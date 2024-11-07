# Sensor Fault Detection ML Project

This project is a machine learning-based application for detecting faults in sensor data. It uses Flask as a web framework, Docker for containerization, GitHub Actions for CI/CD, and MongoDB for data storage. The application can be deployed locally, on AWS EC2, or through Amazon ECR/ECS using an automated pipeline.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Ingestion from MongoDB](#data-ingestion-from-mongodb)
- [Cloud Deployment on AWS EC2](#cloud-deployment-on-aws-ec2)
- [CI/CD Pipeline](#cicd-pipeline)
- [File Structure](#file-structure)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The goal of this project is to build an ML pipeline that can detect faults in sensor data. The pipeline includes data ingestion, preprocessing, model training, and prediction. This repository contains the necessary files for building, training, and deploying the model using Flask as the web framework.

## Features
- **Data Ingestion**: Retrieves data from MongoDB and saves it as a CSV file for further processing.
- **Training Pipeline**: Trains a model based on input sensor data.
- **Prediction Pipeline**: Accepts sensor data to detect faults and provides predictions.
- **Error Handling**: Custom exception handling for efficient debugging.
- **Logging**: Logs important events and errors throughout the training and prediction processes.
- **CI/CD**: GitHub Actions automate integration, delivery, and deployment.
- **Containerization**: Docker is used to package the application for deployment.

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask
- Docker (if deploying with Docker)
- MongoDB (for data storage)
- AWS credentials (if deploying to Amazon ECR/ECS)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sensor-fault-detection.git
    cd sensor-fault-detection
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

## Usage

### Training
To start training the model, navigate to `http://localhost:5000/train` in your web browser or use a tool like `curl`:
```bash
curl http://localhost:5000/train
