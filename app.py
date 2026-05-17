import streamlit as st
from components.navbar import sidebar_navigation
from components.dashboard import show_dashboard
from components.charts import show_chart
from utils.analyzer import run_flake8, run_bandit, run_radon, format_code
from utils.scoring import calculate_score
from utils.pdf_report import generate_pdf

st.set_page_config(page_title="CodeInsight AI", layout="wide")

menu = sidebar_navigation()

if menu == "Dashboard":
    show_dashboard()

elif menu == "Analyze Code":

    st.title("📂 Upload & Analyze Python Code")

    uploaded_file = st.file_uploader("Upload Python File", type=["py"])
    code_input = st.text_area("Or Paste Code Here", height=300)

    code = ""
    if uploaded_file:
        code = uploaded_file.read().decode()
    elif code_input:
        code = code_input

    if st.button("🚀 Analyze Code") and code:

        style = run_flake8(code)
        security = run_bandit(code)
        complexity = run_radon(code)
        formatted = format_code(code)

        score = calculate_score(style, security, complexity)

        st.subheader("💎 Code Health Score")
        st.metric("Overall Score", f"{score}/100")

        show_chart(
            len(style.splitlines()),
            len(security.splitlines()),
            len(complexity.splitlines()),
        )

        tabs = st.tabs([
            "🎨 Style",
            "🔒 Security",
            "📈 Complexity",
            "🔁 Refactored Code",
        ])

        with tabs[0]:
            st.code(style or "No Style Issues Found")

        with tabs[1]:
            st.code(security or "No Security Issues Found")

        with tabs[2]:
            st.code(complexity or "No Complexity Warnings")

        with tabs[3]:
            col1, col2 = st.columns(2)
            col1.subheader("Original Code")
            col1.code(code)

            col2.subheader("Formatted Code")
            col2.code(formatted)

        if st.button("⬇ Download PDF Report"):
            pdf_path = generate_pdf(score, style, security, complexity)

            with open(pdf_path, "rb") as f:
                st.download_button(
                    "Download Report",
                    f,
                    file_name="CodeInsight_Report.pdf",
                )

elif menu == "About":
    st.title("ℹ About CodeInsight AI")
    st.write("""
    CodeInsight AI is an AI-powered intelligent code review platform 
    that analyzes Python programs for:
    - Style issues
    - Security vulnerabilities
    - Complexity warnings
    - Code formatting
    - Overall quality score
    """)
