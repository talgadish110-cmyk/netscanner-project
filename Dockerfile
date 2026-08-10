# Python slim image

FROM python:3.11-slim



# Set working directory inside the container

WORKDIR /app



# Copy only the script file into the container

COPY scanner.py ./



# Install required libraries

RUN pip install --no-cache-dir requests



# Set default entrypoint command to run the scanner

ENTRYPOINT ["python3", "scanner.py"]
