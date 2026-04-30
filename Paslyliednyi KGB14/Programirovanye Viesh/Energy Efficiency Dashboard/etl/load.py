from database.connection import engine

def load_data(df, table_name="energy_readings"):
    df.to_sql(table_name, engine, if_exists="replace", index=False)


def load_alerts(df, table_name="alerts"):
    df.to_sql(table_name, engine, if_exists="replace", index=False)
