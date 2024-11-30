import streamlit as st
import pandas as pd
import joblib
import pickle
#from google.colab import files

# Upload the model file
#uploaded = files.upload()

# Load the model from the uploaded file
model = joblib.load('models/child_mortality_predictor.pkl')


# Feature names and their descriptions
feature_info = {
    'Year': "The year in which the data was recorded. This represents the specific year for which child mortality is being predicted.",
    'Share of population covered by health insurance (ILO (2014))': 
        "Percentage of the population covered by health insurance, according to the International Labour Organization (ILO). Higher coverage typically correlates with better healthcare access.",
    'BCG (% of one-year-olds immunized)': 
        "The percentage of one-year-old children who received the Bacillus Calmette-Guérin (BCG) vaccine, which protects against tuberculosis.",
    'HepB3 (% of one-year-olds immunized)': 
        "Percentage of one-year-old children who received the third dose of the Hepatitis B vaccine.",
    'Hib3 (% of one-year-olds immunized)': 
        "Percentage of one-year-old children who received the third dose of the Haemophilus influenzae type b (Hib) vaccine, which protects against bacterial infections.",
    'MCV1 (% of one-year-olds immunized)': 
        "Percentage of one-year-old children who received the first dose of the measles-containing vaccine (MCV1), which protects against measles.",
    'Pol3 (% of one-year-olds immunized)': 
        "Percentage of one-year-old children who received the third dose of the polio vaccine, which protects against poliomyelitis.",
    'RCV1 (% of one-year-olds immunized)': 
        "Percentage of one-year-old children who received the first dose of the rotavirus vaccine, which protects against severe diarrhea.",
    'DTP3 (% of one-year-olds immunized)': 
        "Percentage of one-year-old children who received the third dose of the diphtheria, tetanus, and pertussis (DTP) vaccine, which protects against these serious diseases."
}

# Title of the app
st.title("Child Mortality Prediction App")
st.write("### Predict the child mortality rate using healthcare indicators.")

# Sidebar for user input
st.sidebar.header("Input Parameters")
user_inputs = {}

# Dynamically create input fields for all features using number_input
for feature in feature_info:
    user_inputs[feature] = st.sidebar.number_input(feature, value=0, format="%d")
    st.sidebar.tooltip(feature_info[feature])  # Add tooltip with description for each feature

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
