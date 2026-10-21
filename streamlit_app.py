from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Chỉ đường Học viện",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.iframe(
    Path(__file__).with_name("app.html"),
    height=900,
    alt="Bản đồ chỉ đường Học viện",
)
