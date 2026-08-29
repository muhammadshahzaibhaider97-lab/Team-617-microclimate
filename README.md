# 🌡️ FortyGuard Microclimate Heat Dashboard — Team 617

An interactive urban thermal analytics and microclimate visualization platform built for the FortyGuard hackathon challenge.

## 🚀 Key Features

* **Real-Time Microclimate Analytics**: Evaluates Surface Temperature (°C), Air Temperature (°C), Heat Index (°C), and Urban Heat Island (UHI) Risk Intensity.
* **Interactive Target Area Mapping**: Displays precise geographic positioning using dynamic pandas and Streamlit map overlays for presets (Dubai Downtown, Riyadh Center, Abu Dhabi Corniche) or custom inputs.
* **Comparative Thermal Profiling**: Generates responsive, interactive bar charts powered by Plotly Express to compare heat metrics side by side.
* **Strategic Urban Mitigation**: Delivers targeted cooling recommendations (such as urban canopy expansion and reflective pavement deployment) based on microclimate intensity.
* **API Integration & Fallback**: Designed for seamless connectivity with the FortyGuard API, featuring a mock data fallback mode for testing without an API key.

---

## 🛠️ Tech Stack

* **Frontend & Framework**: Streamlit
* **Data Visualization**: Plotly Express, Pandas
* **API & Environment**: Requests, Python-Dotenv
* **Language**: Python 3.14+

---

## 🏃 Getting Started

### Prerequisites
Install the required dependencies using `pip`:

```bash
python -m pip install streamlit requests pandas plotly python-dotenv
