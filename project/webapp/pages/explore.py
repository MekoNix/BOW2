import streamlit as st
from pages.modules.upbar import *

def show_explore_page():
    
    show_up()
    
    # Создаем контейнер с красивым оформлением
    with st.container():
        # Заголовок страницы
        st.markdown("""
            <h1 style='text-align: center; color: #FF9D00; 
            font-family: "Segoe UI", sans-serif; margin-bottom: 2rem;'>
            Explore Heroes
            </h1>
        """, unsafe_allow_html=True)
        

        st.image("pages/static/media/placeholder.png")
        

if __name__ == "__main__":
    params = dict(st.query_params)
    current_page = params.get("page", ["explore"])[0]
    if current_page == "explore":
        show_explore_page()