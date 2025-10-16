import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("F1_modeling.pkl")

st.title("Race Predictor")
st.write(" if they’ll finish the race (1) or not (0).")

year = st.number_input("Year", min_value=1950, max_value=2025)
grid = st.number_input("Starting Grid Position", min_value=1, max_value=30)
laps = st.number_input("Laps Completed", min_value=0, max_value=100)
points = st.number_input("Driver Points", min_value=0.0)
fastestLapTime = st.number_input("Fastest Lap Time (seconds)", min_value=0.0)
rank = st.number_input("Driver Rank", min_value=1, max_value=100)
country = st.text_input("Country", "UK")

input_data = pd.DataFrame({
    "year": [year],
    "grid": [grid],
    "laps": [laps],
    "points": [points],
    "fastestLapTime": [fastestLapTime],
    "rank": [rank],
    "country": [country.lower()],
})

from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
input_data["country"] = enc.fit_transform(input_data["country"])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted target finish: {int(prediction)}")
