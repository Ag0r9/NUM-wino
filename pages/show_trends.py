import pandas as pd
import streamlit as st

st.title('Sugestie cen')

@st.cache_data
def get_trends():
    return pd.read_csv("data/output/trends").rename(columns={
        "Unnamed: 0": "Indeks wina",
        "current_price": "obecna cena",
        "suggested_price":"sugerowana cena",
        "trend":"zmiana ceny"})

df = get_trends()

st.dataframe(df)