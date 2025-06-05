import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Food Pathogen Risk Simulator",
    page_icon="🧪",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton>button {
        background-color: #0366d6;
        color: white;
    }
    .risk-high {
        color: #e63946;
        font-weight: bold;
    }
    .risk-medium {
        color: #ff6f61;
        font-weight: bold;
    }
    .risk-low {
        color: #2a9d8f;
        font-weight: bold;
    }
    .buy-me-coffee {
        background-color: #FF5E5B !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
        text-decoration: none !important;
        display: inline-block !important;
        font-size: 16px !important;
        margin: 4px 2px !important;
        cursor: pointer !important;
        transition: background-color 0.3s !important;
    }
    .buy-me-coffee:hover {
        background-color: #FF3B38 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🧪 Food Pathogen Risk Simulator")
st.markdown("""
    Simulate the growth and risk level of foodborne pathogens based on environmental and handling variables.
    """)

# Sidebar inputs
st.sidebar.header("Simulation Parameters")

# Buy Me A Coffee button in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(
    '<a href="https://ko-fi.com/cirewire" target="_blank" class="buy-me-coffee">☕ Buy Me A Coffee</a>',
    unsafe_allow_html=True
)
st.sidebar.markdown("---")

# Food type selection
food_types = ["Poultry", "Dairy", "Produce", "Seafood"]
selected_food = st.sidebar.selectbox("Food Type", food_types)

# Temperature input
temperature = st.sidebar.slider(
    "Temperature (°C)",
    min_value=0.0,
    max_value=50.0,
    value=25.0,
    step=0.5
)

# Time abuse slider
time_abuse = st.sidebar.slider(
    "Time Abuse (hours)",
    min_value=0,
    max_value=72,
    value=24,
    step=1
)

# pH slider
ph = st.sidebar.slider(
    "pH Level",
    min_value=3.5,
    max_value=7.5,
    value=6.5,
    step=0.1
)

# Water activity slider
water_activity = st.sidebar.slider(
    "Water Activity (aw)",
    min_value=0.85,
    max_value=1.0,
    value=0.95,
    step=0.01
)

# Growth model function
def gompertz_growth(t, N0, r, K):
    return N0 * np.exp(r * t) / (1 + (N0/K) * (np.exp(r * t) - 1))

# Calculate growth parameters based on conditions
def calculate_growth_parameters(temp, ph, aw):
    # Base growth rate (simplified model)
    r = 0.1 * (temp / 25) * (1 - abs(ph - 6.5) / 3.5) * (aw - 0.85) / 0.15
    # Maximum population
    K = 1e9
    # Initial population
    N0 = 1e3
    return N0, r, K

# Generate time points
t = np.linspace(0, time_abuse, 100)

# Calculate growth parameters
N0, r, K = calculate_growth_parameters(temperature, ph, water_activity)

# Calculate growth curve
N = gompertz_growth(t, N0, r, K)

# Create growth curve plot
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=t,
    y=N,
    mode='lines',
    name='Pathogen Growth',
    line=dict(color='#0366d6', width=2)
))

fig.update_layout(
    title='Pathogen Growth Over Time',
    xaxis_title='Time (hours)',
    yaxis_title='Population (CFU/g)',
    template='plotly_white',
    showlegend=True
)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Calculate risk level
def calculate_risk_level(N_final, temp, ph, aw):
    risk_score = (N_final / 1e6) * (temp / 25) * (1 / (1 + abs(ph - 6.5))) * (aw / 0.95)
    
    if risk_score > 0.7:
        return "High", "#e63946"
    elif risk_score > 0.3:
        return "Medium", "#ff6f61"
    else:
        return "Low", "#2a9d8f"

risk_level, risk_color = calculate_risk_level(N[-1], temperature, ph, water_activity)

# Display risk level
st.markdown(f"""
    <div style='text-align: center; padding: 20px; background-color: {risk_color}20; border-radius: 10px;'>
        <h2 style='color: {risk_color};'>Risk Level: {risk_level}</h2>
    </div>
    """, unsafe_allow_html=True)

# Recommendations based on risk level
st.markdown("### Recommendations")
if risk_level == "High":
    st.markdown("""
        - Immediate action required
        - Discard the food product
        - Review temperature control procedures
        - Check storage conditions
    """)
elif risk_level == "Medium":
    st.markdown("""
        - Use the product immediately
        - Do not store for extended periods
        - Consider additional safety measures
    """)
else:
    st.markdown("""
        - Product is within safe parameters
        - Continue normal handling procedures
        - Maintain current storage conditions
    """)

# Export options
st.sidebar.markdown("---")
if st.sidebar.button("Export Data"):
    # Create a DataFrame with the simulation results
    import pandas as pd
    df = pd.DataFrame({
        'Time (hours)': t,
        'Population (CFU/g)': N
    })
    st.sidebar.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        file_name="pathogen_growth_simulation.csv",
        mime="text/csv"
    ) 