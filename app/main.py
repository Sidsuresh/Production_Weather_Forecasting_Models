import streamlit as st
import requests
from datetime import datetime, timedelta

# Configuration
API_BASE_URL = "https://advmla-at2-25548684-latest.onrender.com"

st.set_page_config(
    page_title="Sydney Weather Predictor",
    page_icon="🌦️",
    layout="centered"
)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose a Prediction Task", ["Rain Forecast (7-Day)", "Precipitation Volume (3-Day)"])

st.sidebar.markdown("---")
st.sidebar.info(
    "This app uses a FastAPI backend to process weather data from Open-Meteo "
    "and run ML inferences for Sydney, AU."
)

# --- App Header ---
st.title("🌦️ Sydney Weather Predictor")
st.markdown(f"**Target Location:** Sydney (Lat: -33.86, Lon: 151.20)")

# ==========================================
# Task 1: Binary Rain Prediction (+7 Days)
# ==========================================
if app_mode == "Rain Forecast (7-Day)":
    st.header("Rain-or-Not Prediction")
    st.write("Predicts whether it will rain exactly 7 days after the selected date.")
    
    selected_date = st.date_input("Select an input date", datetime.now(), max_value=datetime.now())
    
    if st.button("Predict Rain Status"):
        with st.spinner("Fetching data and running model..."):
            try:
                date_str = selected_date.strftime("%Y-%m-%d")
                response = requests.get(f"{API_BASE_URL}/predict/rain/", params={"date": date_str})
                
                if response.status_code == 200:
                    data = response.json()
                    res = data["prediction"]
                    
                    st.divider()
                    col1, col2 = st.columns(2)
                    col1.metric("Target Date", res["date"])
                    
                    if res["will_it_rain"]:
                        col2.error("🌧️ Prediction: Rain Expected")
                    else:
                        col2.success("☀️ Prediction: No Rain")
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Connection failed: {e}")

# ==========================================
# Task 2: Cumulative Precipitation (3 Days)
# ==========================================
else:
    st.header("Precipitation Volume Forecast")
    st.write("Predicts the total cumulative precipitation (mm) for the 72-hour window following the selected date.")
    
    selected_date = st.date_input("Select start date", datetime.now(), max_value=datetime.now())
    
    if st.button("Calculate Precipitation"):
        with st.spinner("Processing weather metrics..."):
            try:
                date_str = selected_date.strftime("%Y-%m-%d")
                response = requests.get(f"{API_BASE_URL}/predict/precipitation/fall/", params={"date": date_str})
                
                if response.status_code == 200:
                    data = response.json()
                    res = data["prediction"]
                    
                    st.divider()
                    st.subheader("Forecast Results")
                    
                    # Layout with metrics
                    m_col1, m_col2 = st.columns(2)
                    m_col1.metric("Start Date", res["start_date"])
                    m_col2.metric("End Date", res["end_date"])
                    
                    # Display the result prominently
                    precip = res["precipitation_fall"]
                    st.metric("Estimated Cumulative Fall", f"{precip} mm")
                    
                    # Visual aid
                    if precip > 0:
                        st.info(f"The model expects approximately {precip}mm of water accumulation.")
                    else:
                        st.success("No significant precipitation expected for this period.")
                        
                else:
                    st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
            except Exception as e:
                st.error(f"Connection failed: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Data source: Open-Meteo Historical Archive API")