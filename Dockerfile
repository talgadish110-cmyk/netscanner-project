FROM python:3.9-alpine

WORKDIR /app

COPY scanner.py .

CMD ["python", "scanner.py"]
