import time
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Smart Chassis Vibration Analysis",
    page_icon="🚗",
    layout="wide",
)

st.title("🚗 Smart Chassis Vibration Analysis System")
st.caption("Module 4 • Software simulation for chassis vibration monitoring")

st.info(
    "This is a software simulation using generated acceleration data. "
    "Thresholds are demonstration settings, not validated automotive safety limits. "
    "High vibration does not by itself confirm a crack or structural damage."
)

with st.sidebar:
    st.header("Simulation settings")
    sample_rate = st.slider("Sampling rate (Hz)", min_value=20, max_value=200, value=100, step=10)
    duration = st.slider("Duration (seconds)", min_value=5, max_value=30, value=15)
    scenario = st.selectbox(
        "Vibration scenario",
        ["Normal road", "Moderate vibration", "High vibration event", "Sudden impact"],
    )
    caution_threshold = st.slider("Caution threshold (m/s²)", 0.1, 5.0, 1.5, 0.1)
    warning_threshold = st.slider("Warning threshold (m/s²)", 0.5, 10.0, 3.0, 0.1)
    run_button = st.button("▶ Run simulation", type="primary", use_container_width=True)

def generate_data(rate: int, seconds: int, mode: str) -> pd.DataFrame:
    rng = np.random.default_rng()
    n = rate * seconds
    t = np.arange(n) / rate

    # Simulated dynamic acceleration (m/s²), not real vehicle data.
    base = {
        "Normal road": 0.25,
        "Moderate vibration": 1.2,
        "High vibration event": 3.0,
        "Sudden impact": 0.35,
    }[mode]

    ax = base * np.sin(2 * np.pi * 2.0 * t) + rng.normal(0, base * 0.15 + 0.04, n)
    ay = base * 0.7 * np.sin(2 * np.pi * 1.4 * t + 0.8) + rng.normal(0, base * 0.13 + 0.04, n)
    az = base * 1.1 * np.sin(2 * np.pi * 3.1 * t + 0.4) + rng.normal(0, base * 0.18 + 0.05, n)

    if mode == "High vibration event":
        start, end = int(n * 0.45), int(n * 0.72)
        ax[start:end] += 2.8 * np.sin(2 * np.pi * 7 * t[start:end])
        ay[start:end] += 2.2 * np.sin(2 * np.pi * 6 * t[start:end])
        az[start:end] += 3.5 * np.sin(2 * np.pi * 8 * t[start:end])

    if mode == "Sudden impact":
        idx = int(n * 0.55)
        width = max(1, int(rate * 0.08))
        pulse = np.exp(-np.linspace(0, 5, width)) * 6.0
        stop = min(n, idx + width)
        ax[idx:stop] += pulse[: stop - idx]
        ay[idx:stop] += 0.7 * pulse[: stop - idx]
        az[idx:stop] += 1.2 * pulse[: stop - idx]

    magnitude = np.sqrt(ax**2 + ay**2 + az**2)
    return pd.DataFrame({
        "Time (s)": t,
        "X acceleration (m/s²)": ax,
        "Y acceleration (m/s²)": ay,
        "Z acceleration (m/s²)": az,
        "Vibration magnitude (m/s²)": magnitude,
    })

if run_button:
    df = generate_data(sample_rate, duration, scenario)
    st.session_state["vibration_data"] = df
    st.session_state["scenario"] = scenario
    st.session_state["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if "vibration_data" not in st.session_state:
    st.write("Choose a scenario in the sidebar, then click **Run simulation** to generate sample data.")
    st.markdown("""
    **What this simulation demonstrates**
    1. Simulated three-axis acceleration measurements.
    2. Calculation of vibration magnitude.
    3. Threshold-based normal, caution, and warning classification.
    4. A time-series chart and downloadable CSV log.
    """)
    st.stop()

df = st.session_state["vibration_data"]
scenario_used = st.session_state["scenario"]
peak = float(df["Vibration magnitude (m/s²)"].max())
rms = float(np.sqrt(np.mean(df["Vibration magnitude (m/s²)"] ** 2)))
mean_mag = float(df["Vibration magnitude (m/s²)"].mean())

if peak >= warning_threshold:
    status, color, symbol = "WARNING — HIGH VIBRATION", "red", "🔴"
elif peak >= caution_threshold:
    status, color, symbol = "CAUTION — MODERATE VIBRATION", "orange", "🟠"
else:
    status, color, symbol = "NORMAL — WITHIN DEMO THRESHOLD", "green", "🟢"

st.subheader(f"{symbol} System status: {status}")
st.caption(f"Scenario: **{scenario_used}** • Generated: {st.session_state.get('created_at', '—')}")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Peak magnitude", f"{peak:.2f} m/s²")
m2.metric("RMS magnitude", f"{rms:.2f} m/s²")
m3.metric("Mean magnitude", f"{mean_mag:.2f} m/s²")
m4.metric("Samples collected", f"{len(df):,}")

fig = go.Figure()
for col, name in [
    ("X acceleration (m/s²)", "X axis"),
    ("Y acceleration (m/s²)", "Y axis"),
    ("Z acceleration (m/s²)", "Z axis"),
]:
    fig.add_trace(go.Scatter(x=df["Time (s)"], y=df[col], mode="lines", name=name))
fig.update_layout(
    title="Acceleration by axis over time",
    xaxis_title="Time (seconds)",
    yaxis_title="Dynamic acceleration (m/s²)",
    hovermode="x unified",
    legend_title="Sensor axis",
)
st.plotly_chart(fig, use_container_width=True)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=df["Time (s)"],
    y=df["Vibration magnitude (m/s²)"],
    mode="lines",
    name="Magnitude",
))
fig2.add_hline(y=caution_threshold, line_dash="dash", annotation_text="Caution threshold")
fig2.add_hline(y=warning_threshold, line_dash="dash", annotation_text="Warning threshold")
fig2.update_layout(
    title="Vibration magnitude and demonstration thresholds",
    xaxis_title="Time (seconds)",
    yaxis_title="Magnitude (m/s²)",
    hovermode="x unified",
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Event summary")
if peak >= warning_threshold:
    st.error("Abnormal vibration threshold exceeded. In a real vehicle, this would be an alert for inspection—not proof of chassis damage.")
elif peak >= caution_threshold:
    st.warning("Caution threshold reached. Review the vibration data and operating conditions.")
else:
    st.success("The simulated vibration stayed below the caution threshold.")

st.subheader("Sample data")
st.dataframe(df.head(20), use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇ Download complete data as CSV",
    data=csv,
    file_name="chassis_vibration_data.csv",
    mime="text/csv",
)

with st.expander("Method and limitations"):
    st.markdown("""
    - Acceleration is simulated independently for the X, Y, and Z axes.
    - Vibration magnitude is calculated as `sqrt(ax² + ay² + az²)`.
    - The dashboard classifies the **peak magnitude** against user-selected thresholds.
    - The generated values are illustrative and are not measurements from a real vehicle.
    - Real chassis health assessment requires calibrated sensors, gravity/bias handling,
      suitable filtering and frequency analysis, vehicle-specific baselines, and validation
      against physical inspection or other reference methods.
    """)
