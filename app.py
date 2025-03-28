import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    # Replace with the actual file path
    return pd.read_csv("clustered_data.csv")

# Load the data
df = load_data()

# Ensure the "Cluster_k" column exists before proceeding
if "Cluster_k" not in df.columns:
    st.error("Error: Column 'Cluster_k' not found in DataFrame")
else:
    # Retrieve unique cluster labels
    cluster_labels = sorted(df["Cluster_k"].unique())

    # Sidebar for cluster selection
    selected_cluster = st.sidebar.selectbox("Select Cluster_k", cluster_labels)

    # Filter data for the selected cluster
    cluster_data = df[df["Cluster_k"] == selected_cluster]

    # Set colors for the clusters using Plotly color palette
    cluster_colors = {label: px.colors.qualitative.Set1[i] for i, label in enumerate(cluster_labels)}
    color = cluster_colors[selected_cluster]

    # Set page title
    st.title(f"Cluster_k {selected_cluster} Analysis")

    # Plot histogram of Age distribution based on Gender using Plotly
    fig1 = px.histogram(cluster_data, x="Age_original", color="Gender_Male",
                        nbins=30, title="Age Distribution",
                        labels={"Gender_Male": "Gender"},
                        color_discrete_map={0: color, 1: "gray"})
    st.plotly_chart(fig1)

  

    # Now, generate additional plots using Matplotlib and Seaborn for detailed cluster analysis

    # Define cluster colors for Matplotlib/Seaborn plots
    cluster_colors_matplotlib = {0: 'blue', 1: 'green', 2: 'red', 3: 'orange', 4: 'purple'}

    # Plot Age distribution, divided by Gender_Male using Seaborn/Matplotlib
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.histplot(cluster_data[cluster_data['Gender_Male'] == 0]['Age_original'],
                 kde=True, color=cluster_colors_matplotlib[selected_cluster], label='Female', ax=ax)
    sns.histplot(cluster_data[cluster_data['Gender_Male'] == 1]['Age_original'],
                 kde=True, color='gray', label='Male', ax=ax)
    ax.set_title(f'Age Distribution - Cluster {selected_cluster}')
    ax.legend()
    st.pyplot(fig)

    # Plot Annual Income distribution, divided by Gender_Male using Seaborn/Matplotlib
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.histplot(cluster_data[cluster_data['Gender_Male'] == 0]['Annual_Income (£K)_original'],
                 kde=True, color=cluster_colors_matplotlib[selected_cluster], label='Female', ax=ax)
    sns.histplot(cluster_data[cluster_data['Gender_Male'] == 1]['Annual_Income (£K)_original'],
                 kde=True, color='gray', label='Male', ax=ax)
    ax.set_title(f'Annual Income Distribution - Cluster {selected_cluster}')
    ax.legend()
    st.pyplot(fig)

    # Plot Spending Score distribution, divided by Gender_Male using Seaborn/Matplotlib
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.histplot(cluster_data[cluster_data['Gender_Male'] == 0]['Spending_Score_original'],
                 kde=True, color=cluster_colors_matplotlib[selected_cluster], label='Female', ax=ax)
    sns.histplot(cluster_data[cluster_data['Gender_Male'] == 1]['Spending_Score_original'],
                 kde=True, color='gray', label='Male', ax=ax)
    ax.set_title(f'Spending Score Distribution - Cluster {selected_cluster}')
    ax.legend()
    st.pyplot(fig)

    # # Display cluster statistics in Streamlit
    st.subheader(f"Cluster_k {selected_cluster} Statistics")
    st.write(cluster_data[['Age_original', 'Annual_Income (£K)_original', 'Spending_Score_original']].describe())
