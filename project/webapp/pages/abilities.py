import streamlit as st 
from pages.modules.upbar import *
from pages.modules.jasonstethem import get_json_data

def show_skill_card():
    pass

def show_ab_page():
    # Устанавливаем текущую страницу в session_state
    st.session_state.current_page = "abilities"
    show_up()
    show_skill_card()
    
    st.write("123")
if __name__ == "__main__":
    st.set_page_config(page_title="BOW2 - Abilities", layout="wide")
    params = dict(st.query_params)
    current_page = params.get("page", ["abilities"])[0]
    if current_page == "abilities":
        show_ab_page()