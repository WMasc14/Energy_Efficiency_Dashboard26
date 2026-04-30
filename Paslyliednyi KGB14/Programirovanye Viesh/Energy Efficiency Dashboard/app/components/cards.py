import streamlit as st

def metric_cards(kpis):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Consumo Total (kWh)", kpis["total_kwh"])
    c2.metric("Unidades Produzidas", kpis["total_units"])
    c3.metric("Fator de Potência", kpis["avg_power_factor"])
    c4.metric("kWh / Unidade", kpis["kwh_per_unit"])
