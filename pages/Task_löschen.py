import streamlit as st

def delete_task(self, title):
    if title in st.session_state.tasks:
        del st.session_state.tasks[title]
        st.success(f"🗑 Aufgabe '{title}' wurde gelöscht.")
    else:
        st.warning(f"Aufgabe '{title}' nicht gefunden!")