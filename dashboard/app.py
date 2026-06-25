import streamlit as st
import pandas as pd
from models.inference import stack_predict

st.set_page_config(page_title="Osprey Risk Dashboard", layout="wide")

st.title(" Osprey Fraud Risk Dashboard")

uploaded = st.file_uploader("Upload transactions CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Preview:", df.head())

    if st.button("Score Transactions"):
        scores = stack_predict(df)
        df["fraud_probability"] = scores
        df["risk"] = df["fraud_probability"].apply(
            lambda p: "HIGH" if p > 0.8 else "MEDIUM" if p > 0.5 else "LOW"
        )
        st.success("Scoring complete")
        st.dataframe(df)

        st.download_button(
            "Download Results",
            df.to_csv(index=False),
            file_name="osprey_scored.csv",
            mime="text/csv"
        )
