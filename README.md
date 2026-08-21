# NetScanner Project 🚀

An advanced, automated network scanning and security auditing tool, fully integrated with a modern DevOps CI/CD pipeline.

## 📌 Overview
The NetScanner project features a smart Python script designed to check the availability of specific IPs and ports across a network. The entire system is containerized within a lightweight Docker environment and managed automatically through a robust CI/CD pipeline using GitHub Actions.

## 🛠️ Tech Stack & Tools
* **Python**: Core logic for network scanning and availability checks.
* **Docker & Docker Compose**: Containerization, management, and local environment orchestration.
* **GitHub Actions**: Automation for building the CI/CD pipeline (Build & Push).
* **Docker Hub**: Remote storage and management of Docker Images.

## ⚙️ Project Structure
* `.github/workflows/ci.yml`: Defines the automated CI/CD pipeline triggered on every Push.
* `Dockerfile`: Instructions for building the application's container image.
* `docker-compose.yml`: Local deployment and multi-container execution setup.
* `audit_pipeline.sh`: Automation script for executing security audits.

## 💻 Local Setup & Execution
To run the scanner locally using Docker Compose, execute the following command in your terminal:
```bash
docker-compose up --build
