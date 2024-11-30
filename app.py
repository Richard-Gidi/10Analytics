import streamlit as st
import pandas as pd
import joblib
import pickle

# Load the model from the uploaded file
model = joblib.load('models/child_mortality_predictor.pkl')

# Feature names (adjust as needed)
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

# Welcome page introduction
st.title("Welcome to the Child Mortality Prediction App")
st.write("""
### Goal of SDG 3: Good Health and Well-being
Sustainable Development Goal (SDG) 3 aims to ensure healthy lives and promote well-being for all at all ages. Achieving SDG 3 is vital to addressing the major health challenges facing the world today, from reducing maternal and child mortality rates to tackling communicable diseases such as HIV/AIDS and tuberculosis. It emphasizes the importance of universal health coverage, access to essential health services, and improving health outcomes through investments in healthcare and well-being.

One of the targets within SDG 3 is to reduce child mortality, which remains a significant global issue. Children under the age of five are particularly vulnerable, and efforts are ongoing to ensure that no child dies from preventable causes. This involves improving healthcare systems, increasing vaccination coverage, and providing better access to nutrition and sanitation.

In this app, we aim to support these global efforts by providing a tool to predict child mortality rates based on healthcare indicators. By inputting data such as immunization rates and health insurance coverage, we can gain insights into factors that influence child mortality and work toward better health outcomes.
""")

# Title of the app
st.title("Child Mortality Prediction App")
st.write("### Predict the child mortality rate using healthcare indicators.")

# Sidebar for user input
st.sidebar.header("Input Parameters")
user_inputs = {}

# Dynamically create input fields for all features using number_input
for feature in feature_names:
    user_inputs[feature] = st.sidebar.number_input(feature, value=0, format="%d")

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
