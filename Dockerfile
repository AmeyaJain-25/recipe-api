# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt /code/

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /code/

# Expose port 8000 for the Django application
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
