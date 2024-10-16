import streamlit as st
import joblib
import pandas as pd

# Load the trained model 
model = joblib.load('fault_classifier.pkl')

# Define feature names 
feature_names = ['Ia', 'Ib', 'Ic', 'Va', 'Vb', 'Vc']



# Streamlit App Title

st.title("Fault Prediction Simulator")

Ia = st.number_input("Current Ia (A)", value=0.0)
Ib = st.number_input("Current Ib (A)", value=0.0)
Ic = st.number_input("Current Ic (A)", value=0.0)
Va = st.number_input("Current Va (A)", value=0.0)
Vb = st.number_input("Current Vb (A)", value=0.0)
Vc = st.number_input("Current Vc (A)", value=0.0)

# Predict Fault Type
if st.button("Predict Fault"):
    # converting the input data into a 2D numpy array so that it can be put into the model
    input_data = pd.DataFrame([[Ia, Ib, Ic, Va, Vb, Vc]], columns=feature_names)
    # make a prediction
    fault_type_code = model.predict(input_data)[0]
    # the numeric code is mapped back to the original fault type
    fault_mapping = {0 : "No Fault", 1: "LG Fault", 2:"LL Fault",
                     3:"LLG Fault", 4: "LLL Fault"}
    fault_type =  fault_mapping.get(fault_type_code, "Unknown Fault")
    st.write(f"Predicted Fault Type: {fault_type}")

