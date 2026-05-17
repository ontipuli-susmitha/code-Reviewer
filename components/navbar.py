import streamlit as st
from streamlit_option_menu import option_menu

def sidebar_navigation():
    with st.sidebar:
        selected = option_menu(
            menu_title="🤖 CodeInsight AI",
            options=["Dashboard", "Analyze Code", "About"],
            icons=["speedometer2", "file-earmark-code", "info-circle"],
            menu_icon="robot",
            default_index=0,
        )
    return selected
