import streamlit as st
from utils import load_tasks, save_tasks

st.title("🗑️ Task löschen")

if "tasks" not in st.session_state:
    st.session_state['tasks'] = load_tasks()

if st.session_state['tasks']:
    task_name = st.selectbox("Wähle eine Aufgabe zum Löschen", list(st.session_state['tasks'].keys()), key="task_select")

    if st.button("Aufgabe löschen"):
        if task_name in st.session_state['tasks']:
            del st.session_state['tasks'][task_name]
            save_tasks(st.session_state['tasks'])
            st.success(f"Aufgabe '{task_name}' wurde gelöscht.")
else:
    st.info("Keine Aufgaben vorhanden.")