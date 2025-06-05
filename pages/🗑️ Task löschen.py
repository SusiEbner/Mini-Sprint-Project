import streamlit as st

st.title("🗑️ Task löschen")

if "tasks" not in st.session_state:
    st.session_state.tasks = {}

if st.session_state.tasks:
    task_name = st.selectbox("Wähle eine Aufgabe zum Löschen", list(st.session_state.tasks.keys()), key="task_select")

    if st.button("Aufgabe löschen"):
        del st.session_state.tasks[task_name]
        st.success(f"Aufgabe '{task_name}' wurde gelöscht.")
else:
    st.info("Keine Aufgaben vorhanden.")