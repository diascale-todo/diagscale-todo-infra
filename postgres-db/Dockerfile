# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install the Python dependencies
RUN pip install --no-cache-dir psycopg2

# Set the command to run the db_prep_service script
CMD ["python", "db_prep.py"]

