
# NetScanner Project

Automated network and service availability checker tool.



## What does it do?

A Python script that checks if a specific port on a target IP address is open and listening, packaged inside a lightweight Alpine Linux Docker container for full portability.



## How to run?

1. Build the image: `docker build -t netscanner .`

2. Run the container: `docker run --rm netscanner`

