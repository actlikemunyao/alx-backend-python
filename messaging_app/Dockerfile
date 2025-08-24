# Simple Dockerfile for the Django messaging app
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV DJANGO_SECRET_KEY=docker-secret
EXPOSE 8000

RUN python manage.py collectstatic --noinput || true
RUN python manage.py migrate --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
