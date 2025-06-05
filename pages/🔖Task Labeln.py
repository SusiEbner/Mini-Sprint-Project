import streamlit as st

st.title("🔖Task Labeln")

def label_task(self, title, label):
    if title in st.session_state.tasks:
        st.session_state.tasks[title]["label"] = label
        st.success(f" Label für '{title}' wurde auf '{label}' gesetzt.")
    else:
        st.warning(f"Aufgabe '{title}' nicht gefunden!")