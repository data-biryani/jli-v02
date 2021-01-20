import streamlit as st
import pandas as pd
from judge import Judge

st.sidebar.markdown("# JLI v2")

st.sidebar.markdown("## Upload judge data")
uploaded_csv_judge = st.sidebar.file_uploader("Upload CSV", type="csv", key="judge")
if uploaded_csv_judge:
    df_judge = pd.read_csv(uploaded_csv_judge)
    st.sidebar.write(f"{df_judge.shape[0]} rows and {df_judge.shape[0]} columns")
    
st.sidebar.markdown("## Upload judgment data")
uploaded_csv_judgment = st.sidebar.file_uploader("Upload CSV", type="csv", key="judgment")
if uploaded_csv_judgment:
    df_judgment = pd.read_csv(uploaded_csv_judgment)
    st.sidebar.write(f"{df_judgment.shape[0]} rows and {df_judgment.shape[0]} columns")
    
st.sidebar.markdown("## Upload judgment text data")
uploaded_csv_text = st.sidebar.file_uploader("Upload CSV", type="csv", key="text")
if uploaded_csv_text:
    df_text = pd.read_csv(uploaded_csv_text)
    st.sidebar.write(f"{df_text.shape[0]} rows and {df_text.shape[0]} columns")


mode = st.radio(label="", options=["Judges", "Judgments", "Judgment text"], index=0,)

if mode == "Judges":
    if uploaded_csv_judge:
        st.write(df_judge)
        st.write(df_judge.describe())

if mode == "Judgments":
    if uploaded_csv_judgment:
        st.write(df_judgment)
        st.write(df_judgment.describe())

if mode == "Judgment text":
    if uploaded_csv_text:
        st.write(df_text)
        st.write(df_text.describe())