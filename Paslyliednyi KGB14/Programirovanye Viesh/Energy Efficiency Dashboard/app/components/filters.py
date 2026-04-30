import streamlit as st

def apply_filters(df):
    st.sidebar.header("Filtros")

    lines = st.sidebar.multiselect(
        "Linha",
        options=sorted(df["line_id"].unique()),
        default=sorted(df["line_id"].unique())
    )
    machines = st.sidebar.multiselect(
        "Máquina",
        options=sorted(df["machine_id"].unique()),
        default=sorted(df["machine_id"].unique())
    )

    min_date = df["timestamp"].min().date()
    max_date = df["timestamp"].max().date()
    date_range = st.sidebar.date_input("Período", [min_date, max_date])

    filtered = df[
        (df["line_id"].isin(lines)) &
        (df["machine_id"].isin(machines))
    ]

    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered = filtered[
            (filtered["timestamp"].dt.date >= start_date) &
            (filtered["timestamp"].dt.date <= end_date)
        ]

    return filtered
