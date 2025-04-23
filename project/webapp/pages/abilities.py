import streamlit as st
def navigate_to(page):
   st.switch_page(page)
   
with st.sidebar:
    # Логотип и название
    # Здесь должен быть логотип, но пока используем текст
    st.title("BOW2")
    st.write("Builds in base: 1,328")
    st.write("Last update: Apr 20, 2024")
    
    # Навигационные кнопки
    st.write("## Navigation")
    if st.button("🏠 Home", use_container_width=True):
        navigate_to('pages/home.py')
    
    if st.button("🔨 Create Build", use_container_width=True):
        navigate_to('pages/build.py')
    
    if st.button("🔍 Explore", use_container_width=True):
        navigate_to('pages/explore.py')
    
    if st.button("📊 Abilities", use_container_width=True):
        navigate_to('pages/abilities.py')
    
    # Информация внизу сайдбара
    st.write("---")
    st.write("## Info")
    st.write("X: @X")
    st.write("B2OW2@gmail.com")

def display_abilities_page():
    if st.button("YA"):
        st.warning("Пизда Рулям")