# Sensor Fault Detection ML Project

This project is a machine learning-based application for detecting faults in sensor data. It uses Flask as a web framework, Docker for containerization, GitHub Actions for CI/CD, and MongoDB for data storage. The application can be deployed locally, on AWS EC2, or through Amazon ECR/ECS using an automated pipeline.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Usage](#usage)

## Project Overview
The goal of this project is to build an ML pipeline that can detect faults in sensor data. The pipeline includes data ingestion, preprocessing, model training, and prediction. This repository contains the necessary files for building, training, and deploying the model using Flask as the web framework.

![Input Page](/sensor_output/input.png)
![Output Page](/sensor_output/output.png)


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
## File Structure

The repository contains the following main directories and files:

- **.github/workflows/**: GitHub Actions workflows for CI/CD pipeline.
- **artifacts/**: Stores model artifacts and generated files during execution.
- **config/**: Configuration files for setting up the project.
- **notebooks/**: Jupyter notebooks for data analysis and prototyping.
- **prediction_artifacts/**: Artifacts generated from prediction pipeline.
- **predictions/**: Stores generated predictions.
- **sensor_output/**: Output files related to sensor data processing.
- **src/**: Core source code including pipelines and utility scripts.
- **static/css/**: CSS files for the web interface.
- **templates/**: HTML templates for web pages.

Other important files:
- **app.py**: Main application file for the Flask API.
- **Dockerfile**: Docker configuration for containerization.
- **requirements.txt**: Dependencies required for the project.
- **setup.py**: Installation setup for packaging the project.
- **upload_data.py**: Script for data ingestion from MongoDB.
- **README.md**: Project overview and documentation.
## Usage

### Training
To start training the model, navigate to `http://localhost:5000/train` in your web browser or use a tool like `curl`:
```bash
curl http://localhost:5000/train


