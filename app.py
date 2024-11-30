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

# Create a navigation menu
menu = ["Welcome", "Variable Explanation", "Prediction"]
selection = st.sidebar.radio("Go to", menu)

# Set the theme for the app
st.set_page_config(page_title="Child Mortality Prediction App", page_icon=":guardsman:", layout="wide", initial_sidebar_state="expanded")

# Welcome page content
if selection == "Welcome":
    st.title("Welcome to the Child Mortality Prediction App")
    
    # Add an image to the welcome page
    st.image("models/sdg.jpg", caption="Child Mortality Prediction - SDG 3", use_column_width=True)

    st.write("""
    ### Goal of SDG 3: Good Health and Well-being
    Sustainable Development Goal (SDG) 3 aims to ensure healthy lives and promote well-being for all at all ages. Achieving SDG 3 is vital to addressing the major health challenges facing the world today, from reducing maternal and child mortality rates to tackling communicable diseases such as HIV/AIDS and tuberculosis. It emphasizes the importance of universal health coverage, access to essential health services, and improving health outcomes through investments in healthcare and well-being.

    One of the targets within SDG 3 is to reduce child mortality, which remains a significant global issue. Children under the age of five are particularly vulnerable, and efforts are ongoing to ensure that no child dies from preventable causes. This involves improving healthcare systems, increasing vaccination coverage, and providing better access to nutrition and sanitation.

    In this app, we aim to support these global efforts by providing a tool to predict child mortality rates based on healthcare indicators. By inputting data such as immunization rates and health insurance coverage, we can gain insights into factors that influence child mortality and work toward better health outcomes.
    """)

# Variable Explanation page content
elif selection == "Variable Explanation":
    st.title("Variable Explanation")
    st.write("""
    ### Explanation of Variables Used in the Prediction Model:
    The following healthcare indicators are used to predict child mortality:

    - **Year**: The year for which the data is collected. This helps to account for the impact of time and changes in healthcare systems or policy on child mortality.
    - **Share of population covered by health insurance (ILO (2014))**: The percentage of the population covered by health insurance. A higher percentage of coverage is generally associated with improved healthcare access and lower child mortality.
    - **BCG (% of one-year-olds immunized)**: The percentage of one-year-olds who received the Bacillus Calmette-Guérin (BCG) vaccine, which helps protect against tuberculosis. Vaccination is crucial for reducing preventable deaths in children.
    - **HepB3 (% of one-year-olds immunized)**: The percentage of one-year-olds who received the third dose of the Hepatitis B vaccine. Hepatitis B vaccination reduces the risk of liver disease and associated mortality.
    - **Hib3 (% of one-year-olds immunized)**: The percentage of one-year-olds who received the third dose of the Haemophilus influenzae type b (Hib) vaccine. This vaccine prevents infections like meningitis, pneumonia, and epiglottitis.
    - **MCV1 (% of one-year-olds immunized)**: The percentage of one-year-olds who received the first dose of the Measles, Mumps, and Rubella (MMR) vaccine. Measles vaccination reduces child mortality from this preventable disease.
    - **Pol3 (% of one-year-olds immunized)**: The percentage of one-year-olds who received the third dose of the polio vaccine. Polio vaccination prevents paralysis and death due to the virus.
    - **RCV1 (% of one-year-olds immunized)**: The percentage of one-year-olds who received the first dose of the Rotavirus vaccine. This vaccine reduces the risk of severe diarrhea and dehydration in children.
    - **DTP3 (% of one-year-olds immunized)**: The percentage of one-year-olds who received the third dose of the Diphtheria, Tetanus, and Pertussis (DTP) vaccine. Vaccination helps prevent these deadly diseases in young children.
    """)

# Prediction page content
elif selection == "Prediction":
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
