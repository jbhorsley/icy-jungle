# Use official Python image
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput

# 👇 bind Gunicorn to the PORT provided by the platform
CMD ["sh", "-c", "gunicorn webapp.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
