import streamlit as st

def redirect(page):
    st.session_state.current_page = page.split('/')[-1].split('.')[0]
    st.switch_page(f"pages/{page}.py")

def show_up():

    if 'current_page' not in st.session_state:

        params = dict(st.query_params)
        st.session_state.current_page = params.get("page", ["home"])[0]
    

    with open('pages/static/css/upbar.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    

    st.markdown("""
        <style>
            div.block-container{padding-top: 0.5rem;}
            header {visibility: hidden;}
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    

    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    

    st.markdown('<div class="logo">GitHub</div>', unsafe_allow_html=True)
    

    current_page = st.session_state.get('current_page', 'home')
    
    with st.container():
        col1, col2, col3, col4, col5, col6 = st.columns([0.4, 0.4, 0.5, 0.5, 2, 0.4])
        
        with col1:
            btn_class = "active" if current_page == "home" else ""
            st.markdown(f'<div class="stButton {btn_class}">', unsafe_allow_html=True)
            if st.button("⌂Home", key="home_btn", help="Home"):
                st.session_state.current_page = "home"
                redirect("home")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            btn_class = "active" if current_page == "build" else ""
            st.markdown(f'<div class="stButton {btn_class}">', unsafe_allow_html=True)
            if st.button("◈Build ", key="build_btn", help="Build"):
                st.session_state.current_page = "build"
                redirect("build")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            btn_class = "active" if current_page == "explore" else ""
            st.markdown(f'<div class="stButton {btn_class}">', unsafe_allow_html=True)
            if st.button("◎Explore", key="explore_btn", help="Explore"):
                st.session_state.current_page = "explore"
                redirect("explore")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            btn_class = "active" if current_page == "abilities" else ""
            st.markdown(f'<div class="stButton {btn_class}">', unsafe_allow_html=True)
            if st.button("✧Abilities", key="abilities_btn", help="Abilities"):
                st.session_state.current_page = "abilities"
                redirect("abilities")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col5:
            st.markdown(f'<p class="header-text">Last update: <strong>{None}</strong></p>', unsafe_allow_html=True)
        with col6:
            st.markdown(f'<p class="header-text">Builds in base: <strong>{None}</strong></p>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

