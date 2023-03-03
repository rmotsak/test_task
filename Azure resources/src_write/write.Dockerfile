# Base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the Python script to the working directory
COPY script.py .

# Install dependencies
RUN pip install azure-storage-queue

# Set the command to run the script
CMD ["python", "script.py"]
