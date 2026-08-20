FROM python:3.8-alpine

WORKDIR /app

COPY ./scanner.py .

 COPY ./ips.txt .
 
Install dependencies if needed

RUN pip install requests

ENTRYPOINT ["python3"]

CMD ["scanner.py"]
