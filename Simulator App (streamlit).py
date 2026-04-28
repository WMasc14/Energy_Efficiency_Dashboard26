import streamlit as st
import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="ReactorLab", layout="wide")

# ----------------------------
# Premium CSS
# ----------------------------
st.markdown("""
<style>
body {background: linear-gradient(180deg,#0e1117,#0b0f14);} 
.block-container {padding-top: 1.5rem;}
[data-testid="stMetric"] {
    background-color:#151a24;
    padding:12px;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Title
# ----------------------------
st.title("🧪 ReactorLab")
st.caption("CSTR Simulator • Scenario Comparison Dashboard")

# ----------------------------
# Sidebar - Scenario A
# ----------------------------
st.sidebar.header("⚙️ Scenario A")
CA0_A = st.sidebar.slider("Inlet Concentration A", 0.1, 5.0, 2.0, key="CA0_A")
F_A = st.sidebar.slider("Flow Rate A", 0.1, 5.0, 1.0, key="F_A")
V_A = st.sidebar.slider("Volume A", 1.0, 20.0, 10.0, key="V_A")
k_A = st.sidebar.slider("Reaction Rate A", 0.01, 1.0, 0.3, key="k_A")

# ----------------------------
# Sidebar - Scenario B
# ----------------------------
st.sidebar.header("⚙️ Scenario B")
CA0_B = st.sidebar.slider("Inlet Concentration B", 0.1, 5.0, 1.5, key="CA0_B")
F_B = st.sidebar.slider("Flow Rate B", 0.1, 5.0, 1.2, key="F_B")
V_B = st.sidebar.slider("Volume B", 1.0, 20.0, 8.0, key="V_B")
k_B = st.sidebar.slider("Reaction Rate B", 0.01, 1.0, 0.5, key="k_B")

simulation_time = st.sidebar.slider("Time Horizon", 5, 50, 20)

# ----------------------------
# Model
# ----------------------------
def cstr(CA, t, F, V, CA0, k):
    return (F/V)*(CA0 - CA) - k*CA

# ----------------------------
# Solve both scenarios (auto-run)
# ----------------------------
t = np.linspace(0, simulation_time, 200)

CA_A = odeint(cstr, CA0_A, t, args=(F_A, V_A, CA0_A, k_A)).flatten()
CA_B = odeint(cstr, CA0_B, t, args=(F_B, V_B, CA0_B, k_B)).flatten()

# Metrics

def metrics(CA0, CA, F, V, k):
    tau = V/F
    Da = k*V/F
    X = (CA0 - CA[-1]) / CA0
    return tau, Da, X

tau_A, Da_A, X_A = metrics(CA0_A, CA_A, F_A, V_A, k_A)
tau_B, Da_B, X_B = metrics(CA0_B, CA_B, F_B, V_B, k_B)

# ----------------------------
# Top Metrics
# ----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Conversion A", f"{X_A*100:.1f}%")
    st.metric("Conversion B", f"{X_B*100:.1f}%")

with col2:
    st.metric("Damköhler A", f"{Da_A:.2f}")
    st.metric("Damköhler B", f"{Da_B:.2f}")

with col3:
    st.metric("Residence Time A", f"{tau_A:.2f}")
    st.metric("Residence Time B", f"{tau_B:.2f}")

st.markdown("---")

# ----------------------------
# Plot Comparison
# ----------------------------
fig = go.Figure()

fig.add_trace(go.Scatter(x=t, y=CA_A, mode='lines', name='Scenario A'))
fig.add_trace(go.Scatter(x=t, y=CA_B, mode='lines', name='Scenario B'))

fig.update_layout(
    template="plotly_dark",
    title="Scenario Comparison",
    xaxis_title="Time",
    yaxis_title="Concentration",
    hovermode="x unified"
)

st.plotly_chart(fig, width='stretch')

# ----------------------------
# Insight Panel
# ----------------------------
st.subheader("🧠 Engineering Insight")

if X_A > X_B:
    st.success("Scenario A achieves higher conversion")
elif X_B > X_A:
    st.success("Scenario B achieves higher conversion")
else:
    st.info("Both scenarios perform similarly")

if Da_A > Da_B:
    st.write("Scenario A is more reaction-dominated")
else:
    st.write("Scenario B is more reaction-dominated")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Built for portfolio • Interactive engineering dashboard")
