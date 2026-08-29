import os
import requests
import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
API_KEY = os.getenv("FORTYGUARD_API_KEY", "")

# 2. Page Configuration
st.set_page_config(
    page_title="FortyGuard Heat Insights | Team 617",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ FortyGuard Microclimate Heat Dashboard")
st.caption("Team 617 | Climate-Tech & Urban Thermal Analytics")

# 3. Sidebar Inputs & Location Selection
st.sidebar.header("Location Parameters")
api_key_input = st.sidebar.text_input("FortyGuard API Key", value=API_KEY, type="password")

preset = st.sidebar.selectbox("Choose a city:", ["Custom", "Dubai Downtown", "Riyadh Center", "Abu Dhabi Corniche"])

if preset == "Dubai Downtown":
    lat, lon = 25.2048, 55.2708
elif preset == "Riyadh Center":
    lat, lon = 24.7136, 46.6753
elif preset == "Abu Dhabi Corniche":
    lat, lon = 24.4672, 54.3646
else:
    lat = st.sidebar.number_input("Latitude", value=25.2048, format="%.4f")
    lon = st.sidebar.number_input("Longitude", value=55.2708, format="%.4f")

# 4. API Function (with mock fallback for testing)
def fetch_fortyguard_data(latitude, longitude, key):
    """Fetches microclimate data from FortyGuard API."""
    if not key:
        return {
            "surface_temp_c": 42.5,
            "air_temp_c": 38.2,
            "heat_index_c": 46.1,
            "humidity_pct": 55,
            "urban_heat_island_intensity": "High",
            "cooling_recommendation": "Increase urban canopy cover by 25% and deploy reflective cool pavement coatings in high-density pedestrian zones."
        }, None

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    params = {"latitude": latitude, "longitude": longitude}
    url = "https://api.fortyguard.com/v1/temperature"

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            return response.json(), None
        else:
            return None, f"API Error ({response.status_code}): {response.text}"
    except Exception as e:
        return None, str(e)

# 5. Main Dashboard View
if st.button("🚀 Analyze Heat Microclimate", type="primary"):
    with st.spinner("Fetching thermal analytics..."):
        data, error = fetch_fortyguard_data(lat, lon, api_key_input)

        if error:
            st.error(error)
        else:
            st.success(f"Data Loaded Successfully for Location: ({lat}, {lon})")
            
            # Key Metrics Display
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Surface Temp", f"{data.get('surface_temp_c', 'N/A')} °C")
            col2.metric("Air Temp", f"{data.get('air_temp_c', 'N/A')} °C")
            col3.metric("Heat Index", f"{data.get('heat_index_c', 'N/A')} °C")
            col4.metric("UHI Risk Level", data.get("urban_heat_island_intensity", "Moderate"))

            st.markdown("---")

            # Layout: Map + Interactive Chart Side by Side
            col_map, col_chart = st.columns(2)

            with col_map:
                st.subheader("📍 Target Area Location")
                map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
                st.map(map_data, zoom=12)

            with col_chart:
                st.subheader("📊 Temperature Profile Comparison")
                temp_df = pd.DataFrame({
                    'Metric': ['Air Temp (°C)', 'Surface Temp (°C)', 'Heat Index (°C)'],
                    'Temperature': [
                        data.get('air_temp_c', 0),
                        data.get('surface_temp_c', 0),
                        data.get('heat_index_c', 0)
                    ]
                })
                fig = px.bar(
                    temp_df, 
                    x='Metric', 
                    y='Temperature', 
                    color='Metric',
                    text='Temperature',
                    title="Thermal Breakdown"
                )
                st.plotly_chart(fig, use_container_width=True)

            # Urban Mitigation Insights
            st.subheader("💡 Strategic Cooling Recommendation")
            st.info(data.get("cooling_recommendation", "No specific mitigation recommendation available for this zone."))