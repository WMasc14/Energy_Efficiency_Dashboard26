import streamlit as st
from app.components.cards import metric_cards
from app.components.charts import consumption_by_line, consumption_over_time
from app.components.filters import apply_filters

def render_overview(df, kpis):
    filtered_df = apply_filters(df)
    filtered_kpis = kpis  # KPIs globais, não filtrados

    st.title("Dashboard de Eficiência Energética")
    metric_cards(filtered_kpis)
    consumption_over_time(filtered_df)
    consumption_by_line(filtered_df)
