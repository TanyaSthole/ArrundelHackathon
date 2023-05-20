import streamlit as st
import pandas as pd

st.write("# 🌽 Seed Co Crop Yield Model")

# import the data
df = pd.read_csv("./dataset.csv")
# visualize the data

# Box Plot
crops = df["Crop Yield  (bushels/acre)"].unique

# Bar chart
# Pie chart
# Scatter plot
# 