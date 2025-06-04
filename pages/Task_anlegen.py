import streamlit as st

def add_task(self, title, due_date, label):
    st.session_state.tasks[title] = {"date": due_date, "label": label, "done": False}
    st.success(f"✨ Aufgabe '{title}' wurde hinzugefügt.")