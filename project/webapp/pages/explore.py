import streamlit as st
from pages.modules.apply_css import setup_page  

def show_explore_page():
    gif_location = "pages/static/media/placeholder.png"
    st.image(gif_location)

if __name__ == "__main__":
    st.set_page_config(page_title="Abilities", layout="wide")
    setup_page()
    show_explore_page() 
