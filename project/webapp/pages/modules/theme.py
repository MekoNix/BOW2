import streamlit as st

def apply_dark_theme():
    st.markdown("""
        <style>
        .stApp {
            background-color: #13151a;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stButton>button {
            background-color: #2a2d35;
            color: #ffffff;
            border: none;
        }
        .stButton>button:hover {
            background-color: #3a3d45;
        }
        div[data-testid="stToolbar"] {
            display: none;
        }
        div[data-testid="stDecoration"] {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)