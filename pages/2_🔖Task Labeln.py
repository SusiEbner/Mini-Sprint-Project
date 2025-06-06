import streamlit as st
import pandas as pd 

from utils import load_tasks, save_tasks

st.title("🔖Task Labeln")

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = load_tasks()

task_name = st.text_input("Aufgabenname", key="task_name")
task_label = st.selectbox("Label", ["UNI", "Arbeit", "Freizeit", "Sonstiges"], key="task_label")

if task_name and st.button("Label auswählen"):
    if task_name in st.session_state['tasks']:
        st.session_state['tasks'][task_name]["label"] = task_label
        save_tasks(st.session_state['tasks'])
        st.success(f" Label für '{task_name}' wurde auf '{task_label}' gesetzt.")
    else:
        st.warning(f"Aufgabe '{task_name}' nicht gefunden!")

