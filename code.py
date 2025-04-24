import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Tableau de bord de l'éducation rurale")

uploaded_file = st.file_uploader("📥 Téléversez le fichier CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df["taux_abandon"] = (df["inscrits"] - df["presents"]) / df["inscrits"] * 100
    df["taux_reussite"] = df["admis"] / df["presents"] * 100

    annee = st.selectbox("Année", df["annee"].unique())
    data = df[df["annee"] == annee]

    fig1 = px.bar(data, x="ecole", y="taux_abandon", color="village", title="Taux d'abandon scolaire")
    st.plotly_chart(fig1)

    fig2 = px.bar(data, x="ecole", y="taux_reussite", color="village", title="Taux de réussite")
    st.plotly_chart(fig2)

    st.dataframe(data)
else:
    st.info("Veuillez charger un fichier CSV pour commencer.")
