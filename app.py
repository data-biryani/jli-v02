import streamlit as st
import pandas as pd


st.sidebar.markdown("# JLI v2")

st.markdown
uploaded_csv = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=False)
if uploaded_csv:
    df = pd.read_csv(uploaded_csv)
    st.write(df)
    st.write(df.describe())