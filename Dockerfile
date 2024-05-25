# Use a slim Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies using Pipenv
RUN pip install pipenv

# Install project dependencies
RUN pipenv install --system

# Copy project code
COPY . .

# Expose port for the Flask server (modify if needed)
EXPOSE 5000

# Run the development command with Pipenv
CMD ["pipenv", "shell", "inv", "dev"]
