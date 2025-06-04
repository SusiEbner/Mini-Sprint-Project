
import streamlit as st
from datetime import date

class TaskManager:
    def __init__(self):
        if "tasks" not in st.session_state:
            st.session_state.tasks = {}

    def add_task(self, title, due_date, label):
        st.session_state.tasks[title] = {"date": due_date, "label": label, "done": False}
        st.success(f"✅ Aufgabe '{title}' wurde hinzugefügt.")

    def delete_task(self, title):
        if title in st.session_state.tasks:
            del st.session_state.tasks[title]
            st.success(f"🗑 Aufgabe '{title}' wurde gelöscht.")
        else:
            st.warning(f"⚠ Aufgabe '{title}' nicht gefunden.")

    def label_task(self, title, label):
        if title in st.session_state.tasks:
            st.session_state.tasks[title]["label"] = label
            st.success(f"🏷 Label für '{title}' wurde auf '{label}' gesetzt.")
        else:
            st.warning(f"⚠ Aufgabe '{title}' nicht gefunden.")

    def mark_done(self, title):
        if title in st.session_state.tasks:
            st.session_state.tasks[title]["done"] = True
            st.success(f"✅ Aufgabe '{title}' wurde als erledigt markiert.")
        else:
            st.warning(f"⚠ Aufgabe '{title}' nicht gefunden.")

    def show_today_tasks(self):
        st.subheader("📅 Aufgaben für heute")
        today = str(date.today())
        found = False
        for title, data in st.session_state.tasks.items():
            if data["date"] == today:
                st.markdown(f"- *{title}* (Label: {data['label']}) {'✅' if data['done'] else ''}")
                found = True
        if not found:
            st.info("Keine Aufgaben für heute gefunden.")

    def show_all_tasks(self):
        st.subheader("📋 Alle Aufgaben")
        if not st.session_state.tasks:
            st.info("Noch keine Aufgaben vorhanden.")
        else:
            for title, data in st.session_state.tasks.items():
                status = "✅ Erledigt" if data["done"] else "🕒 Offen"
                st.markdown(f"- *{title}* | Datum: {data['date']} | Label: {data['label']} | Status: {status}")

# Streamlit App
task_manager = TaskManager()

st.markdown("""
<h1 style='font-size: 40px; margin-bottom: 0;'>🎯 Mission Possible</h1>
<p style='font-size: 22px; color: white; margin-top: 0;'> dein Task Manager</p>
""", unsafe_allow_html=True)

page = st.sidebar.selectbox("Navigation", [
    "Task anlegen", "Task labeln", "Task löschen", "Task abhaken",
    "Heutige anzeigen", "Alle anzeigen"
])

if page == "Task anlegen":
    st.header("➕ Neue Aufgabe anlegen")
    title = st.text_input("Titel der Aufgabe")
    due_date = st.date_input("Fälligkeitsdatum")
    label = st.selectbox("Kategorie", ["Arbeit", "Uni", "Freizeit", "Sonstiges"])
    if st.button("Hinzufügen"):
        if title:
            task_manager.add_task(title, str(due_date), label)
        else:
            st.warning("Bitte gib einen Titel ein.")

elif page == "Task labeln":
    st.header("🏷 Aufgabe labeln")
    title = st.text_input("Titel der Aufgabe")
    new_label = st.selectbox("Neues Label", ["Arbeit", "Uni", "Freizeit", "Sonstiges"])
    if st.button("Label aktualisieren"):
        task_manager.label_task(title, new_label)

elif page == "Task löschen":
    st.header("🗑 Aufgabe löschen")
    title = st.text_input("Titel der Aufgabe")
    if st.button("Löschen"):
        task_manager.delete_task(title)

elif page == "Task abhaken":
    st.header("✅ Aufgabe als erledigt markieren")
    title = st.text_input("Titel der Aufgabe")
    if st.button("Als erledigt markieren"):
        task_manager.mark_done(title)

elif page == "Heutige anzeigen":
    task_manager.show_today_tasks()

elif page == "Alle anzeigen":
    task_manager.show_all_tasks()
