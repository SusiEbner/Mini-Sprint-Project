import streamlit as st
from datetime import date, timedelta

class TaskManager:
    def __init__(self):
        if "tasks" not in st.session_state:
            st.session_state.tasks = {}
            # session state is used to persist tasks across interactions

    def add_task(self, title, due_date, label):
        st.session_state.tasks[title] = {"date": due_date, "label": label, "done": False}
        st.success(f"✨ Aufgabe '{title}' wurde hinzugefügt.")

    def delete_task(self, title):
        if title in st.session_state.tasks:
            del st.session_state.tasks[title]
            st.success(f"🗑 Aufgabe '{title}' wurde gelöscht.")
        else:
            st.warning(f"Aufgabe '{title}' nicht gefunden!")

    def label_task(self, title, label):
        if title in st.session_state.tasks:
            st.session_state.tasks[title]["label"] = label
            st.success(f" Label für '{title}' wurde auf '{label}' gesetzt.")
        else:
            st.warning(f"Aufgabe '{title}' nicht gefunden!")

    def mark_done(self, title):
        if title in st.session_state.tasks:
            st.session_state.tasks[title]["done"] = True
            st.success(f"✨ Aufgabe '{title}' wurde als erledigt markiert.")
        else:
            st.warning(f"Aufgabe '{title}' nicht gefunden!")

    def _format_task_display(self, title, data):
        label_colors = {
            "Arbeit": "#fffa5d6",
            "Uni": "#fe8ace",
            "Freizeit": "#c89eef",
            "Sonstiges": "#c6c9f6"
        }
        color = label_colors.get(data["label"], "#dddddd")
        label_html = f"<span style='background-color:{color}; padding:2px 8px; border-radius:8px; font-size:12px;'>{data['label']}</span>"
        title_html = f"<s>{title}</s>" if data["done"] else title
        return f"- {title_html} {label_html}"

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

    def show_all_tasks(self):
        st.subheader("Alle Aufgaben")
        if not st.session_state.tasks:
            st.info("Noch keine Aufgaben vorhanden.")
        else:
            for title, data in st.session_state.tasks.items():
                task_display = self._format_task_display(title, data)
                status = "Erledigt" if data["done"] else "Noch offen!"
                st.markdown(f"{task_display} <span style='color:gray; font-size:12px;'>({data['date']} – {status})</span>", unsafe_allow_html=True)

# Streamlit App
task_manager = TaskManager()

st.markdown("""
<h1 style='font-size: 40px; margin-bottom: 0; text-align: center;'>
    ✨ Mission Possible ✨
</h1>
<p style='font-size: 22px; color: gray; margin-top: 0; text-align: center;'>
    Dein Task Manager
</p>
""", unsafe_allow_html=True)

