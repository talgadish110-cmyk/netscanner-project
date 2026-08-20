FROM python:3.11-slim



WORKDIR /app



COPY scanner.py .



CMD ["python3", "scanner.py"]
