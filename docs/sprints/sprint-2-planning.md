📄 sprint-2-planning.md

Sprint 2 – Planning Document
Sprint Dates: Nov 1 – Nov 12 , 2025
Sprint Goal: Deploy a working Django/Python web application (“Social Butterfly”) connected to a PostgreSQL database, publicly accessible on Render, showing dynamic data from the database.

Selected User Stories

Issue #	Title	Story Points	Priority	Owner
#1	User registration and login	3	High	Backend
#2	Event creation and display in feed	5	High	Backend
#3	Homepage showing dynamic content from DB	3	High	Frontend
#4	Deploy Django app to Render	5	High	DevOps
#5	Configure PostgreSQL instance on Render	3	High	Backend
#6	Basic unit test for user model	2	Medium	QA
#7	Setup CI/CD pipeline (manual Git push deploy)	3	Medium	DevOps

Total Committed Story Points: 24
Team Capacity: 24 points (4 members × ~6 points each)

Dependencies and Risks

Risk 1: Render deployment may require environment variable configuration changes.

Risk 2: Initial PostgreSQL connection errors could delay testing.

Risk 3: Auth package incompatibility with Render deployment.

Mitigation: Early deployment testing (week 1), pair programming for auth setup, daily check-ins.
