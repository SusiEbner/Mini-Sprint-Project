import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = {}

st.title("ToDo abhacken")

def mark_done(self, title):
    if title in st.session_state.tasks:
        st.session_state.tasks[title]["done"] = True
        st.success(f"✨ Aufgabe '{title}' wurde als erledigt markiert.")
    else:
        st.warning(f"Aufgabe '{title}' nicht gefunden!")