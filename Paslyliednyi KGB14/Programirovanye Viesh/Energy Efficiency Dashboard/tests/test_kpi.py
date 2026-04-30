import pandas as pd
from models.kpi import calculate_kpis

def test_calculate_kpis():
    df = pd.DataFrame({
        "kwh": [100, 200],
        "units_produced": [10, 20],
        "power_factor": [0.9, 0.95]
    })

    result = calculate_kpis(df)

    assert result["total_kwh"] == 300
    assert result["total_units"] == 30
    assert result["kwh_per_unit"] == 10.0
