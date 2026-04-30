import streamlit as st
from app.components.filters import apply_filters

def render_alarms(df):
    filtered_df = apply_filters(df)

    st.title("Alarmes e Anomalias")
    threshold = filtered_df["kwh"].mean() + 2 * filtered_df["kwh"].std()
    alarms = filtered_df[filtered_df["kwh"] > threshold]

    st.metric("Qtd. Alarmes", len(alarms))
    st.dataframe(alarms[["timestamp", "machine_id", "line_id", "kwh"]])
