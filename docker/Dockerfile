# Use the official Python 3.10.13 base image
FROM python:3.10.13

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from the local machine to the /app directory in the container
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt using pip
RUN pip install -r requirements.txt

# Expose port 8000 to allow external connections to the application
EXPOSE 8000
