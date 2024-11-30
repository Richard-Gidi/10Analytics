import streamlit as st
import pandas as pd
import joblib
import pickle
#from google.colab import files

# Upload the model file
#uploaded = files.upload()

# Load the model from the uploaded file
model = joblib.load('models/child_mortality_predictor.pkl')

# Load feature names (example uses a training DataFrame structure; adjust as needed)
feature_names = [
    'Year',
    'Share of population covered by health insurance (ILO (2014))',
    'BCG (% of one-year-olds immunized)',
    'HepB3 (% of one-year-olds immunized)',
    'Hib3 (% of one-year-olds immunized)',
    'MCV1 (% of one-year-olds immunized)',
    'Pol3 (% of one-year-olds immunized)',
    'RCV1 (% of one-year-olds immunized)',
    'DTP3 (% of one-year-olds immunized)'
]

# Title of the app
st.title("Child Mortality Prediction App")
st.write("### Predict the child mortality rate using healthcare indicators.")

# Sidebar for user input
st.sidebar.header("Input Parameters")
user_inputs = {}

# Dynamically create input fields for all features
for feature in feature_names:
    if "Year" in feature:
        user_inputs[feature] = st.sidebar.number_input(feature, value=2020, step=1, format="%d")
    elif "%" in feature or "Rate" in feature:
        user_inputs[feature] = st.sidebar.slider(feature, 0.0, 100.0, 50.0)
    else:
        user_inputs[feature] = st.sidebar.number_input(feature, value=0)

# Convert user inputs to a DataFrame
input_df = pd.DataFrame([user_inputs])

# Display input data
st.write("### Input Data")
st.write(input_df)

# Make predictions using the loaded model
prediction = model.predict(input_df)
st.write("### Predicted Child Mortality Rate")
st.write(f"{prediction[0]:.2f} deaths per 1,000 children")

# Notes
st.write("""
### Notes:
- Ensure the values you input represent real-world scenarios.
- This tool provides insights to explore SDG 3 healthcare goals.
""")
