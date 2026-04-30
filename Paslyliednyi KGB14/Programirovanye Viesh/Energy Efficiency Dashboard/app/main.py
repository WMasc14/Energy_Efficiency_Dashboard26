import sys
from pathlib import Path

# Adicionar o diretório raiz ao path para importações
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from etl.extract import extract_data
from etl.transform import transform_data
from app.pages.overview import render_overview
from app.pages.machines import render_machines
from app.pages.alarms import render_alarms

st.set_page_config(page_title="Energy Efficiency Dashboard", layout="wide")

def main():
    df = extract_data()
    df, kpis = transform_data(df)

    pages = {
        "Visão Geral": lambda: render_overview(df, kpis),
        "Máquinas": lambda: render_machines(df),
        "Alarmes": lambda: render_alarms(df),
    }

    selected_page = st.sidebar.radio("Navegação", list(pages.keys()))
    pages[selected_page]()


if __name__ == "__main__":
    main()
