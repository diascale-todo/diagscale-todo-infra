# Use the official Python slim image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Upgrade pip
RUN pip install --upgrade pip

# Install psycopg2-binary without needing build dependencies
RUN pip install --no-cache-dir psycopg2-binary

# Copy the current directory contents into the container
COPY . .

# Install the remaining Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the db_prep_service script
CMD ["python", "db_prep.py"]
