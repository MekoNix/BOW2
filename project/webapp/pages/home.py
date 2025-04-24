import streamlit as st
from pages.modules.sidebar import *
from pages.modules.filemanager import get_resource_path
import os
def show_home_page():
    show_sidebar()
             

if __name__ == "__main__":
    # Получаем параметры как словарь
    params = dict(st.query_params)
    # Получаем значение параметра page или используем 'home' по умолчанию
    current_page = params.get("page", ["home"])[0]
    if current_page == "home":
        show_home_page()