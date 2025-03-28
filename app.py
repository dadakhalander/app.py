import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv("clustered_data.csv")  # Replace with actual dataset path

df = load_data()

cluster_labels = sorted(df["Cluster"].unique())
selected_cluster = st.sidebar.selectbox("Select Cluster", cluster_labels)

cluster_data = df[df["Cluster"] == selected_cluster]

cluster_colors = {label: px.colors.qualitative.Set1[i] for i, label in enumerate(cluster_labels)}
color = cluster_colors[selected_cluster]

st.title(f"Cluster {selected_cluster} Analysis")

fig1 = px.histogram(cluster_data, x="Age_original", color="Gender_Male",
                    nbins=30, title="Age Distribution",
                    labels={"Gender_Male": "Gender"},
                    color_discrete_map={0: color, 1: "gray"})
st.plotly_chart(fig1)

st.subheader(f"Cluster {selected_cluster} Statistics")
st.write(cluster_data[['Age_original', 'Annual_Income (£K)_original', 'Spending_Score_original']].describe())
