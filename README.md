🏡 House Price Prediction – ML + Flask Web App

A simple and interactive Machine Learning web application that predicts house prices based on Area, Bedrooms, and Age of the house.
The model is built using Linear Regression, trained on a dataset of house prices, and deployed using Flask with a clean HTML/CSS UI.

🚀 Demo (Screenshot)
Web UI

<img width="987" height="799" alt="Screenshot 2025-11-28 203625" src="https://github.com/user-attachments/assets/a4454f95-e9f0-4190-83f6-9775074b48e6" />

VS Code Project Structure

📌 Features

✔️ Clean and beautiful UI for prediction
✔️ ML Model built using Linear Regression
✔️ Flask backend for serving predictions
✔️ User inputs:

House Age (years)

Bedrooms

Area (sqft)

✔️ Real-time price prediction
✔️ Lightweight and easy to deploy

📂 Project Structure
├── model/
│   └── house_price_model.pkl
├── templates/
│   └── index.html
├── house_data.csv
├── app.py
├── regression.ipynb
├── requirements.txt
└── README.md

🧠 Machine Learning Model

The model is trained using the following features:

Feature	Description
area	Total area in square feet
bedrooms	Number of bedrooms
age	Age of the house in years
Model Code (Summary)

Loaded dataset using Pandas

Separated features (X) and target (y)

Train-test split (80/20)

Trained LinearRegression()

Evaluated using:

Mean Squared Error

Root Mean Squared Error

R² Score

🛠️ Technologies Used
Frontend

HTML

CSS

Backend

Python

Flask

ML Libraries

Scikit-learn

Pandas

NumPy

Joblib for saving/loading model
Below are some screenshots of the UI and backend setup 👇
#MachineLearning #Python #DataScience #MLProjects #Flask #WebDevelopment #LinearRegression #AI
