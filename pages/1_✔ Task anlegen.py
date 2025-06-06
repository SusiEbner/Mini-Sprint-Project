import streamlit as st
import pandas as pd

from utils import load_tasks, save_tasks

if "tasks" not in st.session_state:
    st.session_state['tasks'] = load_tasks()

st.title("Todo anlegen")

task_name = st.text_input("Aufgabenname", key="task_name")
task_label = st.selectbox("Label", ["UNI", "Arbeit", "Freizeit", "Sonstiges"], key="task_label")
task_due = st.date_input("Fälligkeitsdatum", key="task_due")

if st.button("Aufgabe hinzufügen"):
    if task_name not in st.session_state['tasks']:
        st.session_state['tasks'][task_name] = {
            'Beschreibung': task_name,
            'Label': task_label,
            'Fälligkeitsdatum': task_due.isoformat(),
            'done': False
        }
        save_tasks(st.session_state['tasks'])
        st.success(f"Aufgabe '{task_name}' hinzugefügt!")
    else:
        st.warning("Diese Aufgabe existiert bereits.")
else:
    st.error("Bitte gib einen Aufgabenname ein.")