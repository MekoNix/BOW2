import streamlit as st
from pages.modules.upbar import *
from pages.modules.theme import *

def setup_page(page_name):
    """
    Default css setup
    """
    st.query_params.clear()
    if page_name:
        st.session_state.current_page = page_name


    st.markdown("""
        <style>
        .stApp {
            background-color: #13151a;
        }
        .main .block-container {
            padding-top: 0;
            max-width: 100%;
            width: 100%;
            padding-left: 0;
            padding-right: 0;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stButton button {
            background-color: #2a2d35 !important;
            color: #ffffff !important;
            border: none !important;
        }
        .stButton button:hover {
            background-color: #3a3d45 !important;
        }
        div.block-container {
            padding-top: 0 !important;
        }
        div.appview-container {
        margin-top: 0 !important;
        }
        section.main {
        padding-top: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    show_up()
    apply_dark_theme()
    if page_name == "abilities":
        with open('pages/static/css/abilities.css', 'r') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)