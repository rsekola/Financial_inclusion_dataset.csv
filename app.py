import streamlit as st
import pandas as pd
import pickle

# Charger le modèle
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Prédiction d'inclusion financière")
st.write("Entrez les informations de la personne pour prédire si elle possède un compte bancaire.")

# Champs de saisie
age = st.number_input("Âge", min_value=18, max_value=100, value=25)
gender = st.selectbox("Genre (0=Femme, 1=Homme)", [0, 1])
education_level = st.number_input("Niveau d'éducation", min_value=0, max_value=5, value=2)
income = st.number_input("Revenu annuel", min_value=0, value=20000)

# Bouton de prédiction
if st.button("Prédire"):
    data = pd.DataFrame([[age, gender, education_level, income]], 
                        columns=["age", "gender", "education_level", "income"])
    prediction = model.predict(data)[0]
    if prediction == 1:
        st.success("La personne est susceptible de posséder un compte bancaire ✅")
    else:
        st.warning("La personne est peu susceptible de posséder un compte bancaire ❌")
