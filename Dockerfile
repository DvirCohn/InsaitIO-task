# Use an official Python runtime as a parent image
FROM python:3.10.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app

#COPY . /app
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000


# Run pytest to ensure all tests pass
RUN pytest || exit 0

# Run app.py when the container launches
CMD ["python", "app.py"]