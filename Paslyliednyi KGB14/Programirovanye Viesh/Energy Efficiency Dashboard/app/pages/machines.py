import streamlit as st
import plotly.express as px
from app.components.filters import apply_filters

def render_machines(df):
    filtered_df = apply_filters(df)

    st.title("Análise por Máquinas")
    machine_summary = filtered_df.groupby("machine_id", as_index=False).agg({
        "kwh": "sum",
        "units_produced": "sum"
    })
    machine_summary["kwh_per_unit"] = machine_summary["kwh"] / machine_summary["units_produced"]

    fig = px.bar(machine_summary, x="machine_id", y="kwh", title="Consumo por Máquina")
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(machine_summary, x="machine_id", y="kwh_per_unit", title="Eficiência por Máquina")
    st.plotly_chart(fig2, use_container_width=True)
