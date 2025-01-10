# URL Shortener Application

This is a **URL Shortener** application created for the **Modern DevOps Practices** course. It provides an efficient and scalable solution for shortening long URLs into short, shareable links. The application is built using modern DevOps tools and practices, leveraging a CI/CD pipeline for continuous integration and delivery.

## Features

- Shorten URLs with ease
- Built using Python, Flask, and Postgres
- Seamlessly integrates with a CI/CD pipeline for automated testing, linting, security scanning, and deployment
- Supports Docker for containerization and Kubernetes for orchestration

## Prerequisites

To run this app, you will need the following tools and services:

- **Kubernetes Cluster** (e.g., Minikube or a cloud-based Kubernetes service)
- **Docker** for building the application image
- **Postgres** as the database
- **Python 3.11+** and related dependencies
- **GitHub Actions** for CI/CD pipeline (automated tests, security scans, and Docker deployment)

## Running the Application

### Local (Python)

To run the application locally, make sure to have all required dependencies installed. Then, run the application using the `python app.py` command. The app will be available at `http://localhost:5000`.

### Docker

To run the application using Docker, use the `docker-compose up --build` command will build and start the containers, and the app will be available at `http://localhost:5000`.

### Kubernetes

To run the application on Kubernetes, make sure you have docker and minikube installed. If you are running for the first time run the commands in the following order:

- run `minikube start`
- run `kubectl apply -f postgres-secret.yml`
- run `kubectl apply -f postgres.yml`
- run `kubectl apply -f webapp.yml`
- run `kubectl get pods`
- use other command like `kubectl logs <pod-name>` and `kubectl describe services` to further check availability
- run `minikube service webapp-service`. It will open the app in your browser

## CI/CD Pipeline

This project integrates a robust CI/CD pipeline using GitHub Actions to automate the testing, security scans, and deployment of the application. The pipeline consists of the following jobs:

1. **Snyk_Scan**: Scans the repository for vulnerabilities and security issues.
2. **Build-and-Lint**: Installs dependencies, sets up a Python environment, and performs linting on the code.
3. **SonarCloud_Scan**: Performs static analysis of the code using SonarCloud, and runs unit tests with coverage.
4. **Trivy_Scan**: Scans the Docker image for security vulnerabilities.
5. **Publish Docker Image**: Builds and publishes the Docker image to Docker Hub when a release is made.
