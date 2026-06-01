import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Disaster Response AI Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------
# Title Section
# ---------------------------
st.title("🌍 Disaster Response AI")
st.subheader("Predictive Earthquake Hazard & Emergency Priority Dashboard")

st.markdown(
    """
    This dashboard visualizes **real-time earthquake risk intelligence**
    derived from **USGS seismic data** and **machine learning models**.
    It supports **data-driven disaster response and resource planning**.
    """
)

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    event_data = pd.read_csv(r"C:\Users\My Lappy\Downloads\Disaster_AI\outputs\hazard_scores_cleaned.csv")
    regional_data = pd.read_csv(r"C:\Users\My Lappy\Downloads\Disaster_AI\outputs\regional_demand_cleaned.csv")
    return event_data, regional_data

df_events, df_regions = load_data()

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("🔎 Filters")

min_mag, max_mag = st.sidebar.slider(
    "Select Magnitude Range",
    float(df_events["mag"].min()),
    float(df_events["mag"].max()),
    (3.0, float(df_events["mag"].max()))
)

filtered_events = df_events[
    (df_events["mag"] >= min_mag) &
    (df_events["mag"] <= max_mag)
]

# ---------------------------
# KPI Metrics
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🌐 Total Events", len(filtered_events))
col2.metric("⚠️ Avg Priority Index", round(filtered_events["priority_index"].mean(), 3))
col3.metric("🚑 Total Casualties", int(filtered_events["expected_casualties"].sum()))
col4.metric("🆘 Rescue Tasks", int(filtered_events["search_rescue_tasks"].sum()))

# ---------------------------
# Risk Distribution
# ---------------------------
st.markdown("### 📊 High Hazard Risk Distribution")

fig, ax = plt.subplots(figsize=(8,4))
sns.histplot(filtered_events["priority_index"], bins=30, kde=True, ax=ax)
ax.set_xlabel("Priority Index (ML-driven Risk)")
ax.set_ylabel("Count")
st.pyplot(fig)

# ---------------------------
# Top Risk Regions
# ---------------------------
st.markdown("### 🔥 Top High-Risk Regions")

top_regions = df_regions.sort_values(
    "priority_index", ascending=False
).head(10)

st.dataframe(top_regions, use_container_width=True)

# ---------------------------
# Bar Chart: Region Priority
# ---------------------------
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.barplot(
    data=top_regions,
    x="region",
    y="priority_index",
    ax=ax2
)
ax2.set_title("Top 10 Regions by Priority Index")
ax2.set_xlabel("Region")
ax2.set_ylabel("Priority Index")
plt.xticks(rotation=45)
st.pyplot(fig2)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown(
    "📌 **Data Source:** USGS Earthquake Catalog | "
    "**Model:** ML-based Hazard Risk Scoring | "
    "**Use Case:** Emergency Response Planning"
)
