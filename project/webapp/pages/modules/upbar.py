import streamlit as st
from pages.modules.stats import *

def redirect(page):
    st.session_state.current_page = page.split('/')[-1].split('.')[0]
    st.switch_page(f"pages/{page}.py")

def show_up():
    current_page = st.session_state.get('current_page', 'home')
    
    with open('pages/static/css/upbar.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # Подключаем шрифт Material Icons
    st.markdown(
        '<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">',
        unsafe_allow_html=True
    )

    # Скрываем стандартные элементы Streamlit и убираем отступы и скроллбары
    st.markdown("""
        <style>
            div.block-container {padding-top: 0 !important;}
            div.appview-container {margin-top: 0 !important;}
            section.main {padding-top: 0 !important;}
            header {visibility: hidden;}
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            html, body {
                overflow: hidden !important;
                overflow-x: hidden !important;
                overflow-y: hidden !important;
                width: 100% !important;
                height: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            
            ::-webkit-scrollbar {
                display: none !important;
                width: 0 !important;
                height: 0 !important;
            }
            
            * {
                scrollbar-width: none !important;
                -ms-overflow-style: none !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    st.markdown('''<div class="logo" style="font-size: 20px;font-weight: bold;color: #ffffff;padding: 5px 0;font-family: 'Arial', sans-serif;display: flex;align-items: center;gap: 5px;">    OverBuild    <span style="        font-size: 0.6em;        background: #ff5722;        color: white;        padding: 2px 5px;        border-radius: 3px;        vertical-align: middle;    ">BETA</span></div>''', unsafe_allow_html=True)
    
    current_page = st.session_state.get('current_page', 'home')
    col_widths = [0.4, 0.4, 0.5, 0.5, 2, 0.4]
    
    with st.container():
        cols = st.columns(col_widths)
        
        # Home button
        with cols[0]:
            btn_class = "active" if current_page == "home" else ""
            st.markdown(f'<div class="stButton {btn_class}">', unsafe_allow_html=True)
            if st.button("⌂Home", key="home_btn", help="Home"):
                st.session_state.current_page = "home"
                redirect("home")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Build button
        with cols[1]:
            btn_class = "active" if current_page == "build" else ""
            st.markdown(f'<div class="stButton {btn_class}">', unsafe_allow_html=True)
            if st.button("◈Build", key="build_btn", help="Build"):
                st.session_state.current_page = "build"
                redirect("build")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Explore button
        with cols[2]:
            btn_class = "active" if current_page == "explore" else ""
            st.markdown(f'<div class="stButton {btn_class}">', unsafe_allow_html=True)
            if st.button("◎Explore", key="explore_btn", help="Explore"):
                st.session_state.current_page = "explore"
                redirect("explore")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Abilities button
        with cols[3]:
            btn_class = "active" if current_page == "abilities" else ""
            st.markdown(f'<div class="stButton {btn_class}">', unsafe_allow_html=True)
            if st.button("✧Abilities", key="abilities_btn", help="Abilities"):
                st.session_state.current_page = "abilities"
                redirect("abilities")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Version info
        with cols[4]:
            var, data = vercheck()
            if var:
                st.markdown(
                    f'''
                    <p class="header-text">
                        <span style="background-color: #008000; color: white; padding: 4px 8px; border-radius: 12px; font-size: 12px; margin-left: 10px;" title="New releases">
                            <i class="material-icons" style="font-size: 14px; vertical-align: middle;">check</i> Data for verion: <strong>{data}</strong>
                        </span>
                    </p>
                    ''',
                    help="OverBuild version is matching Overwatch version", 
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'''
                    <p class="header-text" title="Data might be outdated">
                        <span style="background-color: #ff4d4d; color: white; padding: 5px 10px; border-radius: 17px; font-size: 14px; margin-left: 10px;" title="New releases">
                            <i class="material-icons" style="font-size: 14px; vertical-align: middle;">new_releases</i> Data for verion: <strong>{data} </strong>
                        </span>
                    </p>
                    ''',
                    help="Overwatch version is newer than OverBuild data version", 
                    unsafe_allow_html=True
                )

        with cols[5]:
            st.markdown(
                f'<p class="header-text">Builds in base: <strong>{None}</strong></p>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)