import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Title
st.title("📊 Random Data Graph Generator")

# Generate Random DataFrame
np.random.seed(42)

data = pd.DataFrame({
    "A": np.random.randint(10, 100, 20),
    "B": np.random.randint(20, 120, 20),
    "C": np.random.randint(5, 80, 20),
    "D": np.random.randint(1, 50, 20)
})

# Show Data
st.subheader("🎲 Random DataFrame")
st.dataframe(data)

# Sidebar Graph Selection
graph_type = st.sidebar.selectbox(
    "Choose Graph Type",
    [
        "Line Chart",
        "Bar Chart",
        "Area Chart",
        "Scatter Plot",
        "Histogram",
        "Pie Chart"
    ]
)

# LINE CHART
if graph_type == "Line Chart":
    st.subheader("📈 Line Chart")
    st.line_chart(data)

# BAR CHART
elif graph_type == "Bar Chart":
    st.subheader("📊 Bar Chart")
    st.bar_chart(data)

# AREA CHART
elif graph_type == "Area Chart":
    st.subheader("📉 Area Chart")
    st.area_chart(data)

# SCATTER PLOT
elif graph_type == "Scatter Plot":
    st.subheader("🔵 Scatter Plot")

    fig, ax = plt.subplots()

    ax.scatter(data["A"], data["B"])

    ax.set_xlabel("Column A")
    ax.set_ylabel("Column B")
    ax.set_title("A vs B")

    st.pyplot(fig)

# HISTOGRAM
elif graph_type == "Histogram":
    st.subheader("📦 Histogram")

    fig, ax = plt.subplots()

    ax.hist(data["A"], bins=5)

    ax.set_title("Distribution of Column A")

    st.pyplot(fig)

# PIE CHART
elif graph_type == "Pie Chart":
    st.subheader("🥧 Pie Chart")

    fig, ax = plt.subplots()

    labels = ["A", "B", "C", "D"]
    values = [
        data["A"].sum(),
        data["B"].sum(),
        data["C"].sum(),
        data["D"].sum()
    ]

    ax.pie(values, labels=labels, autopct="%1.1f%%")

    ax.set_title("Column Contribution")

    st.pyplot(fig)