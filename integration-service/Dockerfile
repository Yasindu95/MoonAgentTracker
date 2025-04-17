# Use an official lightweight Python image as a parent image
FROM public.ecr.aws/docker/library/python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir reduces image size
# --trusted-host pypi.python.org is good practice, especially in constrained networks
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 8001 available to the world outside this container
# (This matches the port your app runs on)
EXPOSE 8001

# Define environment variable (optional, but good practice)
ENV FLASK_APP=integrationService.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8001

# Run app.py when the container launches
# Use gunicorn for production usually, but flask run is ok for simple cases/dev
# CMD ["flask", "run"]
# Alternatively, run directly with python:
CMD ["python", "integrationService.py"]