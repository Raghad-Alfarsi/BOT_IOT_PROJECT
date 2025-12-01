import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# ========== Load Model ==========
model = joblib.load("log_model.pkl")
columns = joblib.load("columns.pkl")

# ========== Load Dataset ==========
df = pd.read_csv("cleaned_data.csv")

st.title("Intrusion Detection System (IDS) Dashboard")

# ======================================
# SECTION 1: Dataset Preview
# ======================================
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ======================================
# SECTION 2: Charts
# ======================================
st.subheader("Attack Distribution")
fig = plt.figure()
sns.countplot(x=df['attack'])
st.pyplot(fig)

st.subheader("Bytes vs Packets (Scatter)")

if 'pkts' in df.columns and 'bytes' in df.columns:
    fig2 = plt.figure()
    sns.scatterplot(
        data=df.sample(2000),
        x='pkts', y='bytes', hue='attack', alpha=0.3
    )
    st.pyplot(fig2)
else:
    st.warning("⚠ Columns pkts or bytes not found!")
    st.write(df.columns)

# ======================================
# SECTION 3: Prediction Area
# ======================================
st.subheader("Real-Time Prediction")

input_data = {}

for col in columns:
    input_data[col] = st.number_input(col, value=0.0)

input_df = pd.DataFrame([input_data])

if st.button("Predict"):
    pred = model.predict(input_df)[0]
    if pred == 0:
        st.success("Normal Traffic")
    else:
        st.error("⚠ Malicious Attack Detected!")