import streamlit as st
from pandas import DataFrame
from datetime import date, timedelta

st.title("🔔Heutige anzeigen")

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = {}

today = date.today()
task_due = st.date_input("Fälligkeitsdatum", key="task_due")

st.title("Heute")

df = DataFrame(st.session_state['tasks'].values())
st.dataframe(df.loc[df["Fälligkeitsdatum"]==task_due])
