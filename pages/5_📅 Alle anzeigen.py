import streamlit as st
import pandas as pd
from datetime import date, timedelta
from utils import load_tasks

st.title("📅 Alle anzeigen")

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = load_tasks()

if st.session_state['tasks']:
    df = pd.DataFrame.from_dict(st.session_state['tasks'], orient='index')

    if "Fälligkeitsdatum" in df.columns:
        df["Fälligkeitsdatum"] = pd.to_datetime(df["Fälligkeitsdatum"]).dt.strftime("%d.%m.%Y")

    st.dataframe(df)
else:
    st.info("Keine Aufgabe vorhanden.")