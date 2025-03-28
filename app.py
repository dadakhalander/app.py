import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv("clustered_data.csv")  # Replace with actual dataset path

# Load data
df = load_data()

# Ensure the "Cluster" column exists before using it
if "Cluster" not in df.columns:
    st.error("Error: Column 'Cluster' not found in DataFrame")
else:
    # Retrieve unique cluster labels
    cluster_labels = sorted(df["Cluster"].unique())

    # Sidebar for cluster selection
    selected_cluster = st.sidebar.selectbox("Select Cluster", cluster_labels)

    # Filter data for the selected cluster
    cluster_data = df[df["Cluster"] == selected_cluster]

    # Set colors for the clusters
    cluster_colors = {label: px.colors.qualitative.Set1[i] for i, label in enumerate(cluster_labels)}
    color = cluster_colors[selected_cluster]

    # Set page title
    st.title(f"Cluster {selected_cluster} Analysis")

    # Plot histogram of age distribution based on gender
    fig1 = px.histogram(cluster_data, x="Age_original", color="Gender_Male",
                        nbins=30, title="Age Distribution",
                        labels={"Gender_Male": "Gender"},
                        color_discrete_map={0: color, 1: "gray"})
    st.plotly_chart(fig1)

    # Display cluster statistics
    st.subheader(f"Cluster {selected_cluster} Statistics")
    st.write(cluster_data[['Age_original', 'Annual_Income (£K)_original', 'Spending_Score_original']].describe())
