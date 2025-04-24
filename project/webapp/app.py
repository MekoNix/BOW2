import streamlit as st

# Устанавливаем параметры для перенаправления на домашнюю страницу
st.query_params["page"] = "home"
st.switch_page("pages/home.py")
