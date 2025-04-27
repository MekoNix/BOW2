import streamlit as st
from pages.modules.apply_css import setup_page



def show_news():
    st.markdown(
        """
        <h1 style='text-align: Left:; color: #ffffff; font-size: 48px; margin-top: 100px;'>
            News
        </h1>
        <p style='text-align: center; color: #cccccc; font-size: 24px;'>
            OverBuild is a new project, and we are constantly working on it. 
            Here you can find the latest news about the project.
        </p>
        """, 
        unsafe_allow_html=True
    )
    # Добавляем отступ перед кнопками
    st.markdown("<br><br>", unsafe_allow_html=True)
    

def show_home_page():
    
    # Main heading с текстом
    st.markdown(
        """
        <h1 style='text-align: center; color: #ffffff; font-size: 48px; margin-top: 100px;'>
            OverBuild
        </h1>
        <p style='text-align: center; color: #cccccc; font-size: 24px;'>
            Create and explore Overwatch 2 builds
        </p>
        """, 
        unsafe_allow_html=True
    )
    # Добавляем отступ перед кнопками
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Create three buttons in a row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔨 CREATE BUILD", use_container_width=True, key="create"):
            st.switch_page("pages/build.py")
            
    with col2:
        if st.button("🔍 EXPLORE BUILDS", use_container_width=True, key="explore"):
            st.switch_page("pages/explore.py")
            
    with col3:
        if st.button("📊 SEARCH ABILITIES", use_container_width=True, key="abilities"):
            st.switch_page("pages/abilities.py")
    show_news()


if __name__ == "__main__":
    st.set_page_config(page_title="OverBuld", layout="wide")
    setup_page(page_name="home")
    show_home_page()