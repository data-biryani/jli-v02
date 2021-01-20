import streamlit as st
import pandas as pd


st.sidebar.markdown("# JLI v2")
mode = st.sidebar.radio(label="", options=["Upload csv", "Judges", "Judgments", "Judgment text"], index=0,)

if mode=="Upload csv":
    st.markdown("## Upload judge data")
    uploaded_csv = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=False)
    if uploaded_csv:
        df = pd.read_csv(uploaded_csv)
        st.write(df)
        st.write(df.describe())
    
    st.markdown("## Upload judgment data")
    uploaded_csv = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=False)
    if uploaded_csv:
        df = pd.read_csv(uploaded_csv)
        st.write(df)
        st.write(df.describe())
    
        st.markdown("## Upload judgment text data")
    uploaded_csv = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=False)
    if uploaded_csv:
        df = pd.read_csv(uploaded_csv)
        st.write(df)
        st.write(df.describe())