# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY . .



RUN apt-get update \
    && apt-get install -y \
        gcc \
        libpq-dev \
        redis-server \
    && rm -rf /var/lib/apt/lists/*
    

# Install dependencies
# RUN pip install --upgrade pip

RUN pip install -r requirements.txt


RUN service redis-server start
#   RUN /etc/init.d/redis-server restart
# RUN celery -A pro worker -l info

# Copy the Django project
COPY pro /app

# Expose the port
EXPOSE 8000

# Run the application
CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000"]
