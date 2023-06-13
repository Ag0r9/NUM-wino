import pickle
import numpy as np
import streamlit as st

@st.cache_resource
def get_model():
    with open("data/models/RFR.p", "rb") as f:
        return pickle.load(f)
    
model = get_model()

st.title('Wyceń wino')

with st.form(key='my_form'):
    fixed_acidity = st.number_input('Fixed Acidity:', value=7.4)
    volatile_acidity = st.number_input('Volatile Acidity:', value=0.62)
    citric_acid = st.number_input('Citric Acid:', value=0.05)
    residual_sugar = st.number_input('Residual sugar:', value=1.9)
    chlorides = st.number_input('Chlorides:', step=0.001, value=0.068)
    free_sulfur_dioxide = st.number_input('Free sulfur dioxide:', value=24)
    total_sulfur_dioxide = st.number_input('Total sulfur dioxide:', value=42)
    density = st.number_input('Density:', step=0.0001, value=0.9961)
    pH = st.number_input('pH:', value=3.42)
    sulphates = st.number_input('Sulphates:', value=0.57)
    alcohol = st.number_input('Alcohol:', value=11.5)
    
    submit_btn = st.form_submit_button('Calculate price')
    
if submit_btn:
    price = model.predict(np.array([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]]))[0].round(2)
    st.subheader(f"Suggested price: {price} EUR")
