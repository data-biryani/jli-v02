import streamlit as st
import pandas as pd
from judge import Judge


st.sidebar.markdown("# JLI v2")
mode = st.sidebar.radio(label="", options=["Upload csv", "Judges", "Judgments", "Judgment text"], index=0,)

if mode=="Upload csv":
    st.markdown("## Upload judge data")
    uploaded_csv_judge = st.file_uploader("Upload CSV", type="csv", key="judge")
    if uploaded_csv_judge:
        df_judge = pd.read_csv(uploaded_csv_judge)
        st.write(df_judge)
        st.write(df_judge.describe())
    
    st.markdown("## Upload judgment data")
    uploaded_csv_judgment = st.file_uploader("Upload CSV", type="csv", key="judgment")
    if uploaded_csv_judgment:
        df_judgment = pd.read_csv(uploaded_csv_judgment)
        st.write(df_judgment)
        st.write(df_judgment.describe())
    
    st.markdown("## Upload judgment text data")
    uploaded_csv_text = st.file_uploader("Upload CSV", type="csv", key="text")
    if uploaded_csv_text:
        df_text = pd.read_csv(uploaded_csv_text)
        st.write(df_text)
        st.write(df_text.describe())