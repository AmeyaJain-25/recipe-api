# Recipe Application

## API Usage and Access to the code

- Github: https://github.com/AmeyaJain-25/recipe-api
- API (hosted on ec2): http://ec2-15-206-67-159.ap-south-1.compute.amazonaws.com/

## Features

- Containerized with Docker
- Asynchronous task handling with Celery
- Sending Email notification on likes of recipe and daily likes

## Technologies

- Docker
- Django
- Django Rest Framework
- Celery
- Redis (for Celery broker)
- PostgreSQL (for database)
- AWS EC2 (for deployment)
- AWS RDS (for postgres db)

## Prerequisites

- Docker and Docker Compose installed on your local machine

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AmeyaJain-25/recipe-api.git
   cd recipe-api
   ```

2. **Environment Variables:**

   Create a .env file in the root directory and add your environment-specific variables. Check **.env.example** for reference

3. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build
   ```

4. **Running the Application:**

   Apply migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

   Create a superuser:

   ```
   bash
   docker-compose exec web python manage.py createsuperuser
   ```

   Start Celery worker:

   ```
   bash
   docker-compose exec web celery -A config worker -l info
   ```

   Start Celery beat (for periodic tasks):

   ```
   bash
   docker-compose exec web celery -A config beat -l info
   ```

   The application should now be running and accessible at http://127.0.0.1:8000
