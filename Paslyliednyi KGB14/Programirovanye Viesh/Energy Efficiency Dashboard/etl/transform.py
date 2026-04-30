from models.kpi import calculate_kpis

def transform_data(df):
    kpis = calculate_kpis(df)
    return df, kpis
