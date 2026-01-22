# Shopper Spectrum

Customer Segmentation and Product Recommendation System using RFM Analysis and Collaborative Filtering.

---

## Problem Statement

The e-commerce industry generates large volumes of transactional data daily. Analyzing this data is essential to understand customer purchase behavior, segment customers effectively, and recommend relevant products to improve customer experience and business growth.

This project focuses on:
- Segmenting customers based on Recency, Frequency, and Monetary (RFM) analysis
- Building a product recommendation system using item-based collaborative filtering

---

## Dataset

Online Retail transactional dataset containing:
- Invoice numbers
- Product details
- Purchase quantities
- Transaction timestamps
- Customer identifiers
- Country information

---

## Techniques Used

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- RFM Analysis
- KMeans Clustering
- Elbow Method and Silhouette Score
- Item-Based Collaborative Filtering (Cosine Similarity)
- Streamlit Application for Deployment

---

## Streamlit App Features

### Product Recommendation Module
- User selects a product
- Application recommends top 5 similar products based on purchase patterns

### Customer Segmentation Module
- Displays customer Recency, Frequency, and Monetary values
- Identifies customer segment:
  - High-Value
  - Regular
  - Occasional
  - At-Risk

---
## Project Structure

Shopper-Spectrum/
│── app.py
│── customer_segments.csv
│── product_recommendations.csv
│── Shopper_Spectrum.ipynb
│── requirements.txt

---

## How to Run the Application

1. Install required libraries:
   pip install -r requirements.txt
2. Run the Streamlit app:
   streamlit run app.py

---

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

## Author

Vedant Mehta

   


