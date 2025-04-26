import streamlit as st
from pages.modules.upbar import *

def show_home_page():
    show_up()
    
    # Main heading
    st.markdown(
        """
        <h1 style='text-align: center; color: #ffffff; font-size: 48px; margin-top: 100px;'>
        </h1>
        """, 
        unsafe_allow_html=True
    )
    
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


if __name__ == "__main__":
    st.set_page_config(page_title="BOW2", layout="wide")
    params = dict(st.query_params)
    current_page = params.get("page", ["home"])[0]
    if current_page == "home":
        show_home_page()