import streamlit as st
import pandas as pd

# ---------------- APP CONFIG ----------------
st.set_page_config(page_title="Shopper Spectrum", layout="wide")

st.title("🛒 Shopper Spectrum")
st.subheader("Customer Segmentation & Product Recommendation")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    segments = pd.read_csv("customer_segments.csv")
    recommendations = pd.read_csv("product_recommendations.csv")
    return segments, recommendations

segments, recs = load_data()

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Choose Module:",
    ("Product Recommendation", "Customer Segmentation")
)

# ---------------- PRODUCT RECOMMENDATION ----------------
if option == "Product Recommendation":
    st.header("🎯 Product Recommendation System")

    product = st.selectbox("Select a Product", recs['Product'])

    row = recs[recs['Product'] == product]

    st.subheader("Recommended Products")
    for i in range(1, 6):
        st.write("🔹", row[f"Rec{i}"].values[0])

# ---------------- CUSTOMER SEGMENTATION ----------------
else:
    st.header("👥 Customer Segmentation")

    customer = st.selectbox("Select Customer ID", segments['CustomerID'])

    customer_data = segments[segments['CustomerID'] == customer].iloc[0]

    st.metric("Recency (days)", customer_data['Recency'])
    st.metric("Frequency", customer_data['Frequency'])
    st.metric("Monetary Value", round(customer_data['Monetary'], 2))

    st.success(f"Customer Segment: **{customer_data['Segment']}**")
