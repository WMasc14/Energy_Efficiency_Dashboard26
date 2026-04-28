import numpy as np
from scipy.integrate import odeint

# CSTR model

def cstr(CA, t, F, V, CA0, k):
    return (F/V)*(CA0 - CA) - k*CA


def run_simulation(params):
    t = np.linspace(0, params["time"], 200)

    CA = odeint(
        cstr,
        params["CA0"],
        t,
        args=(params["F"], params["V"], params["CA0"], params["k"])
    ).flatten()

    return {
        "time": t.tolist(),
        "CA": CA.tolist()
    }