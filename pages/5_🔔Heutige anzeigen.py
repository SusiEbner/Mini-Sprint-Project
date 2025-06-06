import streamlit as st
import pandas as pd
from datetime import date, timedelta
from utils import load_tasks

st.title("🔔Heutige anzeigen")

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = load_tasks()

task_due = st.date_input("Fälligkeitsdatum", value=date.today(), key="task_due")

if st.session_state['tasks']:
    df = pd.DataFrame(st.session_state['tasks'].values())

    df["Fälligkeitsdatum"] = pd.to_datetime(df["Fälligkeitsdatum"]).dt.date

    gefiltert = df[df["Fälligkeitsdatum"] == task_due]

    st.subheader(f" Aufgaben für {task_due.strftime('%d.%m.%Y')}")
    st.dataframe(gefiltert)
else:
    st.info("Keine Aufgaben vorhandenn.")
