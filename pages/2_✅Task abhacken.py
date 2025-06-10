import streamlit as st
from utils import load_tasks, save_tasks

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

st.title("ToDo abhacken")

tasks = st.session_state.tasks

open_tasks = {k: v for k, v in tasks.items() if not v.get("done", False)}

if open_tasks:
   for title, task in open_tasks.items():

    checked = st.checkbox(title, value=False, key=title)

    if checked:
        tasks[title]["done"] = True
        save_tasks(tasks)
        st.rerun()

else:
    st.info("🎉 Keine offenen Aufgaben mehr.")