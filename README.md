# F1_Modeling
Overview
A machine learning project to predict Formula 1 race performance using historical race data. The model is trained with a Random Forest regressor, and the app is deployed with Streamlit for interactive predictions.

Features
Data preprocessing with label encoding

Model training and evaluation (MAE, RMSE, R²)

Streamlit app to upload data, test the model and view predictions

Installation
bash
pip install streamlit pandas numpy scikit-learn joblib
Run the App
bash
streamlit run app.py
Upload your CSV data and make predictions interactively.

Inputs for Testing
Provide features like year, round, grid, positionOrder, points, laps, milliseconds, fastestLap, rank, driverRef (encoded), constructorRef (encoded), circuitRef (encoded), and others as per the training set.