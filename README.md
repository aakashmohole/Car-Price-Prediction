# Car Price Prediction Project 🏎️🚗

🦄 This project aims to predict the price of used cars based on various features such as model, mileage, year, and so on. It includes a web application for users to input car details and get predicted prices. Additionally, the project uses Docker for containerization and deployment.

## Project Structure 🎗️

- `data/`: Contains the dataset used for training the model.
- `models/`: Contains the trained machine learning models.
- `app/`: Contains the source code for the web application.
- `Dockerfile`: Dockerfile for containerizing the web application.
- `requirements.txt`: List of Python dependencies for the project.

## Features 👨‍💻

- Predict the price of used cars based on input features.
- User-friendly web interface for inputting car details.
- Dockerized application for easy deployment.

## Web Application 📲

The web application allows users to input details about a car, such as model, year, mileage, fuel type, and transmission type. Based on these details, the application predicts the price of the car using a Random Forest model trained on a dataset of historical car prices.

To run the web application locally, follow these steps:
1. Clone this repository.
2. Navigate to the `app` directory.
3. Install the necessary dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.


### Flask Usage ⬇️
The web application is built using Flask, a Python web framework. Flask provides a simple and lightweight way to create web applications in Python. The application uses Flask to handle HTTP requests, render HTML templates, and serve the machine learning model predictions.

### Live Demo: 
![Live Demo: ](https://github.com/aakashmohole/Car-Price-Prediction/blob/main/Images/Car%20price%20prediction.gif)

## Docker 🐬

The application is Dockerized for easy deployment. Docker allows you to package the application and its dependencies into a container, ensuring consistency and portability across different environments.

To run the application using Docker, follow these steps:
1. Install Docker Desktop on your machine.
2. Build the Docker image using the provided `Dockerfile`:

![Docker](https://github.com/aakashmohole/Car-Price-Prediction/blob/main/Images/DockerTerminal.png)
![Docker](https://github.com/aakashmohole/Car-Price-Prediction/blob/main/Images/Screenshot%202024-03-24%20120139.png)

## Usage

1. Clone this repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd car-price-prediction`
3. Build the Docker image: `docker build -t car-price-prediction .`
4. Run the Docker container: `docker run -d -p 5000:5000 car-price-prediction`

The web application will be accessible at `http://localhost:5000`.

## Random Forest Model

The Random Forest model is trained using the dataset available in the `main.ipynb/` directory. It achieves good accuracy in predicting car prices based on the provided features.

## License

This project is licensed under the MIT License - see the [LICENSE]([LICENSE](https://github.com/aakashmohole/Car-Price-Prediction/blob/main/LICENSE)https://github.com/aakashmohole/Car-Price-Prediction/blob/main/LICENSE) file for details.

