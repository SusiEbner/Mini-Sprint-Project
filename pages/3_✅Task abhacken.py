import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = {}

st.title("ToDo abhacken")

def mark_done(title):
    if title in st.session_state.tasks:
        st.session_state.tasks[title]["done"] = True
        st.success(f"✨ Aufgabe '{title}' wurde als erledigt markiert.")
    else:
        st.warning(f"Aufgabe '{title}' nicht gefunden!")


if "tasks" not in st.session_state:
    st.session_state.tasks = {}

if st.session_state.tasks:
    task_name = st.selectbox("Wähle eine Aufgabe zum Abhacken", list(st.session_state.tasks.keys()), key="task_select")

    if st.button("Aufgabe abhaken"):
        mark_done(task_name)
else:
    st.info("Keine Aufgaben vorhanden.")