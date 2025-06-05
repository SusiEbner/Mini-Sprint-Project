import streamlit as st
from datetime import date, timedelta

st.title("🔔Heutige anzeigen")

def show_today_tasks(self):
        st.subheader("✨Aufgaben für heute")
        today = date.today()
        in_3_days = today + timedelta(days=3)

        today_tasks = []
        upcoming_tasks = []

        for title, data in st.session_state.tasks.items():
            due_date = date.fromisoformat(data["date"])
            task_display = self._format_task_display(title, data)

            if due_date == today:
                today_tasks.append(task_display)
            elif today < due_date <= in_3_days:
                upcoming_tasks.append(task_display)

        if today_tasks:
            st.toast("Diese Aufgaben stehen heute an:")
            for task in today_tasks:
                st.markdown(task, unsafe_allow_html=True)
        else:
            st.info("Keine Aufgaben für heute gefunden!")

        if upcoming_tasks:
            st.markdown("<br><small><b> Aufgaben in den nächsten 3 Tagen:</b></small>", unsafe_allow_html=True)
            for task in upcoming_tasks:
                st.markdown(f"<small>{task}</small>", unsafe_allow_html=True)
