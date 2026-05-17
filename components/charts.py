import streamlit as st
import matplotlib.pyplot as plt

def show_chart(style_count, security_count, complexity_count):
    labels = ["Style Issues", "Security Issues", "Complexity Warnings"]
    values = [style_count, security_count, complexity_count]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel("Count")
    ax.set_title("Code Analysis Overview")

    st.pyplot(fig)
