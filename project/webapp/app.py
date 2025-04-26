import streamlit as st
from pages.modules.upbar import *

# Инициализируем session_state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

st.query_params["page"] = "home"
st.switch_page("pages/home.py")
