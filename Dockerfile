# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --timeout=60 -r requirements.txt


# Copy the rest of the project files
COPY . .

# Expose the application port
EXPOSE 5000

# Command to run your application
CMD ["python", "app.py"]
