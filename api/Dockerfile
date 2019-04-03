# Using lightweight alpine image
# FROM python:3.6-alpine
FROM python:3.6

# Installing packages
RUN apt update

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
