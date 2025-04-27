import streamlit as st 
from pages.modules.upbar import *
from pages.modules.theme import *

def show_build_page():
    # Настройка конфигурации страницы
    st.set_page_config(
        page_title="BOW2 - Build", 
        layout="wide",)

    # Очищаем URL параметры
    st.query_params.clear()
    st.session_state.current_page = "build"

    show_up()
    apply_dark_theme()

if __name__ == "__main__":
    show_build_page()