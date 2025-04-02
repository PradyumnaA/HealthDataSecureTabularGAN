import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
real_data = pd.read_csv('data/breach_report.csv')
synthetic_data = pd.read_csv('synthetic_data.csv')

# Streamlit app header
st.title("Real vs Synthetic Data Comparison")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose a page", ["Home", "Data Comparison", "Synthetic Data"])

# Home page
if app_mode == "Home":
    st.markdown("""
    ## Welcome to the Real vs Synthetic Data Comparison App
    This app allows you to compare real and synthetic breach report data.
    You can explore statistical comparisons, visualizations, and more.
    """)

# Data Comparison page
elif app_mode == "Data Comparison":
    st.markdown("""
    ## Real vs Synthetic Data
    Below, you can compare the statistical summaries and visualizations for both datasets.
    """)

    # Display data summary
    st.subheader("Real Data Summary:")
    st.write(real_data.describe())

    st.subheader("Synthetic Data Summary:")
    st.write(synthetic_data.describe())

    # Plot comparison for a specific column (e.g., 'individuals_affected')
    st.subheader('Distribution Comparison (individuals_affected)')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(real_data['individuals_affected'], color='blue', kde=True, label='Real Data', ax=ax)
    sns.histplot(synthetic_data['individuals_affected'], color='red', kde=True, label='Synthetic Data', ax=ax)
    ax.legend()
    st.pyplot(fig)

# Synthetic Data page
elif app_mode == "Synthetic Data":
    st.markdown("""
    ## Synthetic Data
    Below is the synthetic data generated.
    """)

    # Display synthetic data
    st.dataframe(synthetic_data)
