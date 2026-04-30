import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)
rows = 1000

df = pd.DataFrame({
    "timestamp": pd.date_range("2026-01-01", periods=rows, freq="h"),
    "machine_id": np.random.choice(["M01", "M02", "M03", "M04"], rows),
    "line_id": np.random.choice(["L1", "L2"], rows),
    "kwh": np.random.uniform(20, 150, rows),
    "kw": np.random.uniform(5, 50, rows),
    "units_produced": np.random.randint(10, 200, rows),
    "power_factor": np.random.uniform(0.75, 0.99, rows)
})

output = Path(__file__).resolve().parent / "energy_mock.csv"
df.to_csv(output, index=False)
print(f"Mock data saved to {output}")
