import streamlit as st

def show_dashboard():
    st.title("📊 AI Code Review Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("📁 Files Reviewed", "128")
    col2.metric("⭐ Avg Score", "82/100")
    col3.metric("🔒 Security Alerts", "14")

    st.progress(82)

    st.info("Welcome to CodeInsight AI – Intelligent Code Quality Analyzer")
