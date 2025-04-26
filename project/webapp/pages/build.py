import streamlit as st 

from pages.modules.upbar import *

def show_build_page():
    show_up()

if __name__ == "__main__":
    params = dict(st.query_params)
    current_page = params.get("page", ["build"])[0]
    if current_page == "build":
        show_build_page()