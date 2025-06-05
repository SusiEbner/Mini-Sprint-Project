import streamlit as st
import pandas as pd
if "tasks" not in st.session_state:
    st.session_state['tasks'] = {}

st.title("Todo anlegen")

def add_task(self, title, due_date, label):
    st.session_state.tasks[title] = {"date": due_date, "label": label, "done": False}
    st.success(f"✨ Aufgabe '{title}' wurde hinzugefügt.")