import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------
# Page config
# --------------------------------
st.set_page_config(
    page_title="Bot-IoT Traffic Analysis",
    layout="wide"
)

st.title("Bot-IoT Network Traffic Analysis")
st.write("EDA dashboard based on the cleaned Bot-IoT dataset.")

# --------------------------------
# Load data
# --------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("bot_iot_cleaned_data.csv")

df = load_data()

# --------------------------------
# Sidebar
# --------------------------------
st.sidebar.header("Filter")
attack_type = st.sidebar.selectbox(
    "Traffic Type",
    sorted(df["attack"].unique())
)

filtered_df = df[df["attack"] == attack_type]

# --------------------------------
# Layout
# --------------------------------
col1, col2 = st.columns(2)

# --------------------------------
# 1. Attack vs Normal
# --------------------------------
with col1:
    st.subheader("Attack vs Normal")
    fig, ax = plt.subplots(figsize=(3.5, 3))
    sns.countplot(data=df, x="attack", ax=ax)
    st.pyplot(fig, use_container_width=False)

# --------------------------------
# 2. Attack Categories
# --------------------------------
with col2:
    st.subheader("Attack Categories")
    fig, ax = plt.subplots(figsize=(3.5, 3))
    sns.countplot(
        data=filtered_df,
        x="category",
        order=filtered_df["category"].value_counts().index,
        ax=ax
    )
    plt.xticks(rotation=30)
    st.pyplot(fig, use_container_width=False)

# --------------------------------
# New Row
# --------------------------------
col3, col4 = st.columns(2)

# --------------------------------
# 3. Network Protocols
# --------------------------------
with col3:
    st.subheader("Network Protocols")
    fig, ax = plt.subplots(figsize=(3.5, 3))
    sns.countplot(
        data=filtered_df,
        x="proto",
        order=filtered_df["proto"].value_counts().index,
        ax=ax
    )
    st.pyplot(fig, use_container_width=False)

# --------------------------------
# 4. Packets vs Bytes
# --------------------------------
with col4:
    st.subheader("Packets vs Bytes")
    sample_df = filtered_df.sample(3000, random_state=42)
    fig, ax = plt.subplots(figsize=(3.5, 3))
    sns.scatterplot(
        data=sample_df,
        x="pkts",
        y="bytes",
        alpha=0.4,
        ax=ax
    )
    st.pyplot(fig, use_container_width=False)

# --------------------------------
# 5. Correlation Heatmap
# --------------------------------
st.subheader("Correlation Heatmap")

numeric_df = filtered_df.select_dtypes(include="number")

fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(
    numeric_df.corr(),
    cmap="coolwarm",
    cbar=False,
    ax=ax
)
st.pyplot(fig, use_container_width=False)

# --------------------------------
# Footer
# --------------------------------
st.markdown("---")
st.caption("Bot-IoT EDA Dashboard | Streamlit")