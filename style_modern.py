
import streamlit as st

def set_modern_style():
    st.markdown("""
    <style>
    body { background-color: #f7f9fc; }
    .stApp { font-family: "Segoe UI", sans-serif; color: #333; }
    h1, h2, h3 { color: #2c3e50; }
    .css-1cpxqw2, .css-1d391kg { background-color: #ffffff !important; border: 1px solid #e0e0e0 !important; border-radius: 8px; padding: 1rem; }
    .stButton > button { background-color: #2c7be5; color: white; padding: 0.5em 1.5em; border-radius: 5px; border: none; font-weight: bold; }
    .stButton > button:hover { background-color: #1a5dcc; }
    .stTextInput > div > input { background-color: #f0f4f8; border-radius: 5px; }
    .stSelectbox > div > div { background-color: #f0f4f8; border-radius: 5px; }
    .stDataFrame { font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)
