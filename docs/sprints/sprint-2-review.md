📄 sprint-2-review.md

Sprint 2 – Review Document
Sprint Goal: Deploy working Django app with database to staging (Render).

Result: ✅ Goal achieved — Social Butterfly is live and pulls data from the database.

Staging URL: https://icy-jungle.onrender.com/

What’s Working

User registration and login flow.

Logging in / logging out sessions.

Deployed Django project connected to PostgreSQL.

Basic event model created and migrated.

Technical Setup

Framework: Django (Python)

Database: PostgreSQL (Render instance)

Hosting: Render (staging)

CI/CD: Manual deploy via Git push

Branching Model: main and develop branches

Metrics

Planned story points: 24

Completed story points: 24

Velocity: 24 points/sprint

Completion rate: 100 %

Commits: ~35

Pull Requests merged: 8

Completed User Stories

#1 User registration & login ✅

#2 Event creation & feed display ✅

#3 Homepage dynamic content ✅

#4 Deployment ✅

#5 Database setup ✅

#6 Basic unit test ✅

#7 Manual deploy pipeline ✅

Incomplete Stories
None — all Sprint 2 stories completed.

Lessons Learned

Render deploy process was smoother than expected once DB credentials were set.

Auth and migration setup should be documented for new teammates.

Small, frequent commits kept merge conflicts manageable.

Product Backlog Updates

Added stories for search/filter logic, “My RSVPs” page, and edit/delete events for Sprint 3.
