import streamlit as st
from utils import load_tasks, save_tasks

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

st.title("ToDo abhacken")

if st.session_state['tasks']:
    task_name = st.selectbox("Wähle eine Aufgabe zum Abhaken", list(st.session_state['tasks'].keys()), key="task_select")

    if st.button("Aufgabe abhaken"):
        if task_name in st.session_state['tasks']:
            st.session_state['tasks'][task_name]['done'] = True
            save_tasks(st.session_state['tasks'])
            st.success(f"✨ Aufgabe '{task_name}' wurde als erledigt markiert.")
        else:
            st.warning(f"Aufgabe '{task_name}' nicht gefunden!")
else:
    st.info("Keine Aufgaben vorhanden.")