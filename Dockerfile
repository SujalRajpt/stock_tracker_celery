# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the Django development server by default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
