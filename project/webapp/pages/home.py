import streamlit as st
import os
from pages.abilities import *
from pages.explore import *
def display_home():
    """Display the home page content"""
    
    # Hero section with tagline
    st.markdown("<h1 class='header-text'>FORGE YOUR VICTORY</h1>", unsafe_allow_html=True)
    
    # Featured builds section
    st.subheader("Featured Builds")
    
    # Display featured builds in a grid
    col1, col2, col3 = st.columns(3)
    
    # Recent updates section
    st.subheader("Recent Updates")
    st.markdown("""
    - Added 50+ new builds for Season 15
    - Updated ability descriptions for latest patch
    - New filtering options for hero selection
    """)
    
    # Community stats
    st.subheader("Community")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Active Users", "2,450", "+125")
    with col2:
        st.metric("Build Shares", "8,720", "+310")

# Функция для навигации
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


def main():
    if st.session_state['current_page'] == 'home':
        display_home()

def load_css():
    css_file = os.path.join(os.path.dirname(__file__), "static/style.css")
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("CSS файл не найден. Будут использованы стандартные стили.")

load_css()

# Инициализация сессии
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'





if __name__ == "__main__":
    main()
