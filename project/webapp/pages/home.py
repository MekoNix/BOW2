import streamlit as st
from pages.modules.apply_css import setup_page


def show_disclaimer():
    st.markdown(
        """
        <div style='display: flex; align-items: center; border: 1px solid #444444; background-color: #222222; padding: 10px; border-radius: 5px; margin-top: 20px;'>
            <span style='font-size: 20px; color: #ffaa00; margin-right: 10px;'>&#9888;</span>
            <div style='color: #dddddd; font-size: 16px;'>
                <p>OverBuild is currently in beta. If you encounter any issues, please report them on our <a href="https://github.com/MekoNix/OverBuild/issues" target="_blank" style="color: #ffaa00; text-decoration: underline;">GitHub</a>.</p>
                <p>Also, we know our UI isn't the best—we're programmers, not designers!</p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )


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
    with open("pages/static/db/news.md", "r") as file:
        news = file.read()
    st.markdown(
        f"""
        <div style='background-color: #222222; padding: 20px; border-radius: 5px;'>
            <p style='color: #cccccc; font-size: 18px;'>{news}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    

def show_home_page():
    

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
    show_disclaimer()
    show_news()


if __name__ == "__main__":
    st.set_page_config(page_title="OverBuld", layout="wide")
    setup_page(page_name="home")
    show_home_page()