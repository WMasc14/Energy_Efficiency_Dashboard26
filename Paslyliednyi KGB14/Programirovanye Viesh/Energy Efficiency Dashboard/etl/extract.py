import pandas as pd
from config.settings import MOCK_DIR

def extract_data():
    return pd.read_csv(MOCK_DIR / "energy_mock.csv", parse_dates=["timestamp"])
