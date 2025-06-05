import streamlit as st
from datetime import date, timedelta

st.title("📅 Alle anzeigen")

def show_all_tasks(self):
        st.subheader("Alle Aufgaben")
        if not st.session_state.tasks:
            st.info("Noch keine Aufgaben vorhanden.")
        else:
            for title, data in st.session_state.tasks.items():
                task_display = self._format_task_display(title, data)
                status = "Erledigt" if data["done"] else "Noch offen!"
                st.markdown(f"{task_display} <span style='color:gray; font-size:12px;'>({data['date']} – {status})</span>", unsafe_allow_html=True)
