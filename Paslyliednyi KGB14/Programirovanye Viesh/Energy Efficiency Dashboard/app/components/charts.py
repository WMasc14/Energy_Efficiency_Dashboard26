import plotly.express as px
import streamlit as st

def consumption_by_line(df):
    chart = df.groupby("line_id", as_index=False)["kwh"].sum()
    fig = px.bar(chart, x="line_id", y="kwh", title="Consumo por Linha")
    st.plotly_chart(fig, use_container_width=True)


def consumption_over_time(df):
    chart = df.groupby("timestamp", as_index=False)["kwh"].sum()
    fig = px.line(chart, x="timestamp", y="kwh", title="Consumo ao Longo do Tempo")
    st.plotly_chart(fig, use_container_width=True)
