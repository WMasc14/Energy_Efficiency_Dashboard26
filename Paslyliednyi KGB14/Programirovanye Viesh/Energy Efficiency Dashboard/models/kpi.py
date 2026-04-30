def calculate_kpis(df):
    total_kwh = df["kwh"].sum()
    total_units = df["units_produced"].sum()
    avg_pf = df["power_factor"].mean()
    kwh_per_unit = total_kwh / total_units if total_units else 0

    return {
        "total_kwh": round(total_kwh, 2),
        "total_units": int(total_units),
        "avg_power_factor": round(avg_pf, 3),
        "kwh_per_unit": round(kwh_per_unit, 4)
    }
