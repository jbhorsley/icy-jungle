import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from supabase import create_client, Client


def home(request):
    return HttpResponse("<h1>Hello, world! 🎉</h1>")


@require_http_methods(["GET", "POST"])
def signin(request):
    """
    Combined Sign in / Sign up:
    - POST with action=signin -> Auth with email/password
    - POST with action=signup -> Create user; if session returned, log them in; if email confirmation is required, show info
    """
    error = None
    info = None

    if request.method == "POST":
        action = request.POST.get("action", "signin")
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("password_confirm", "")

        if not email or not password:
            error = "Please enter both email and password."
        else:
            try:
                url = os.getenv("SUPABASE_URL")
                anon_key = os.getenv("SUPABASE_ANON_KEY")
                if not url or not anon_key:
                    error = "Server is missing Supabase credentials."
                else:
                    supabase: Client = create_client(url, anon_key)

                    if action == "signup":
                        if password != password_confirm:
                            error = "Passwords do not match."
                        else:
                            # Create user in Supabase
                            res = supabase.auth.sign_up({"email": email, "password": password})
                            # If email confirmation is disabled, session may be returned immediately.
                            # If confirmation is required, session will be None and user must confirm via email.
                            if getattr(res, "session", None):
                                request.session["sb_access_token"] = res.session.access_token
                                request.session["sb_refresh_token"] = res.session.refresh_token
                                request.session["sb_user_id"] = res.user.id
                                request.session["sb_user_email"] = res.user.email
                                return redirect("home")
                            else:
                                info = "Check your email to confirm your account, then sign in."
                    else:
                        # Default: sign in
                        auth_res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                        if auth_res and auth_res.session and auth_res.user:
                            request.session["sb_access_token"] = auth_res.session.access_token
                            request.session["sb_refresh_token"] = auth_res.session.refresh_token
                            request.session["sb_user_id"] = auth_res.user.id
                            request.session["sb_user_email"] = auth_res.user.email
                            return redirect("home")
                        else:
                            error = "Invalid email or password."
            except Exception:
                # Don’t leak internal details to users
                if action == "signup":
                    error = "Sign up failed. If the email may already exist, try signing in."
                else:
                    error = "Sign in failed. Please check your credentials."

    return render(request, "core/signin.html", {"error": error, "info": info})
