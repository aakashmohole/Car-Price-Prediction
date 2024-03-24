# Car Price Prediction Project

This project aims to predict the price of used cars based on various features such as model, mileage, year, and so on. It includes a web application for users to input car details and get predicted prices. Additionally, the project uses Docker for containerization and deployment.


## Features

- Predict the price of used cars based on input features.
- User-friendly web interface for inputting car details.
- Dockerized application for easy deployment.

## Web Application

The web application allows users to input details about a car, such as model, year, mileage, fuel type, and transmission type. Based on these details, the application predicts the price of the car using a Random Forest model trained on a dataset of historical car prices.

To run the web application locally, follow these steps:
1. Clone this repository.
2. Navigate to the `app` directory.
3. Install the necessary dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.


## Flask Usage
The web application is built using Flask, a Python web framework. Flask provides a simple and lightweight way to create web applications in Python. The application uses Flask to handle HTTP requests, render HTML templates, and serve the machine learning model predictions.
[](https://github.com/aakashmohole/Car-Price-Prediction/blob/main/Images/DockerTerminal.png?raw=true)

## Docker

The application is Dockerized for easy deployment. Docker allows you to package the application and its dependencies into a container, ensuring consistency and portability across different environments.

To run the application using Docker, follow these steps:
1. Install Docker Desktop on your machine.
2. Build the Docker image using the provided `Dockerfile`:
