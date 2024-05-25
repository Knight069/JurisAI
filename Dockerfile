# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container at /app
COPY Pipfile Pipfile.lock /app/

# Install pipenv
RUN pip install pipenv

# Install dependencies
RUN pipenv install --system --deploy

# Copy the current directory contents into the container at /app
COPY . /app/

# Install Redis server
RUN apt-get update && apt-get install -y redis-server

# Expose port 5000 for Flask app and port 6379 for Redis
EXPOSE 5000 6379

# Start Redis server
RUN service redis-server start

# Command to run the Python server
CMD ["pipenv", "run", "inv", "dev"]
