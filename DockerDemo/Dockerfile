FROM python:3.10 # Use the official Python image

WORKDIR /app # Set the working directory in the container
COPY requirements.txt requirements.txt # Copy the requirements file
RUN pip3 install --no-cache-dir -r requirements.txt # Install the dependencies

COPY . . # Copy the current directory contents into the container at /app

CMD ["python", "demo.py"] # Command to run the application