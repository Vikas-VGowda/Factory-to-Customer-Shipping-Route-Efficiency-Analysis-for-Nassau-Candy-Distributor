import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Nassau Candy Route Analysis",
    layout="wide"
)

st.title("🚚 Factory-to-Customer Shipping Route Efficiency Analysis")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("Nassau_Candy_Cleaned.csv")

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

ship_mode = st.sidebar.multiselect(
    "Select Ship Mode",
    df["Ship Mode"].unique(),
    default=df["Ship Mode"].unique()
)

df_filtered = df[
    (df["Region"].isin(region))
    &
    (df["Ship Mode"].isin(ship_mode))
]

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Orders",
    len(df_filtered)
)

col2.metric(
    "Average Lead Time",
    round(df_filtered["Lead Time"].mean(),2)
)

col3.metric(
    "Total Sales",
    f"${df_filtered['Sales'].sum():,.0f}"
)

col4.metric(
    "Total Profit",
    f"${df_filtered['Gross Profit'].sum():,.0f}"
)

# --------------------------------------------------
# LEAD TIME BY REGION
# --------------------------------------------------

st.subheader("Average Lead Time by Region")

region_lead = (
    df_filtered
    .groupby("Region")["Lead Time"]
    .mean()
    .reset_index()
)

fig = px.bar(
    region_lead,
    x="Region",
    y="Lead Time",
    title="Average Lead Time by Region"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# SHIP MODE ANALYSIS
# --------------------------------------------------

st.subheader("Ship Mode Performance")

ship_mode_perf = (
    df_filtered
    .groupby("Ship Mode")["Lead Time"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    ship_mode_perf,
    x="Ship Mode",
    y="Lead Time",
    title="Average Lead Time by Ship Mode"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# TOP 10 FASTEST ROUTES
# --------------------------------------------------

st.subheader("Top 10 Fastest Routes")

fastest = (
    df_filtered
    .groupby("Factory_State_Route")
    .agg(
        Avg_Lead_Time=("Lead Time","mean"),
        Shipments=("Lead Time","count")
    )
    .reset_index()
    .sort_values(
        "Avg_Lead_Time"
    )
    .head(10)
)

st.dataframe(fastest)

# --------------------------------------------------
# BOTTOM 10 ROUTES
# --------------------------------------------------

st.subheader("Bottom 10 Slowest Routes")

slowest = (
    df_filtered
    .groupby("Factory_State_Route")
    .agg(
        Avg_Lead_Time=("Lead Time","mean"),
        Shipments=("Lead Time","count")
    )
    .reset_index()
    .sort_values(
        "Avg_Lead_Time",
        ascending=False
    )
    .head(10)
)

st.dataframe(slowest)

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(df_filtered.head())