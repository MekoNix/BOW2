import streamlit as st


def redirect(page):
    st.switch_page(f"pages/{page}.py")

def show_sidebar():

    with st.sidebar:
    # Логотип и название
    # Здесь должен быть логотип, но пока используем текст
        st.title("BOW2")
        st.write("Builds in base: 1,328")
        st.write("Last update: Apr 20, 2024")
    
        # Навигационные кнопки
        st.write("## Navigation")
        if st.button("🏠 Home", use_container_width=True):
            redirect("home")
    
        if st.button("🔨 Create Build", use_container_width=True):
            redirect("build")
    
        if st.button("🔍 Explore", use_container_width=True):
            redirect("explore")
    
        if st.button("📊 Abilities", use_container_width=True):
            redirect("abilities")
    
        # Информация внизу сайдбара
        st.write("---")
        st.write("## Info")

