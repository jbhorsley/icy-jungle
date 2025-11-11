import os
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from supabase import create_client, Client

from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Hello, world! 🎉</h1>")

@require_http_methods(["GET", "POST"])
def signin(request):
    error = None

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

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
                    # Authenticate with Supabase
                    auth_res = supabase.auth.sign_in_with_password({"email": email, "password": password})

                    if auth_res and auth_res.session and auth_res.user:
                        # Save minimal session info
                        request.session["sb_access_token"] = auth_res.session.access_token
                        request.session["sb_refresh_token"] = auth_res.session.refresh_token
                        request.session["sb_user_id"] = auth_res.user.id
                        request.session["sb_user_email"] = auth_res.user.email
                        return redirect("home")
                    else:
                        error = "Invalid email or password."
            except Exception as e:
                # Avoid leaking details to users; log in real apps
                error = "Sign-in failed. Please check your credentials."

    return render(request, "core/signin.html", {"error": error})
