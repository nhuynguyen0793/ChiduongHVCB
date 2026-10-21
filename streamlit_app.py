from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Chỉ đường Học viện",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    footer {
        display: none;
    }

    [data-testid="stAppViewContainer"] .main,
    [data-testid="stAppViewContainer"] .main .block-container {
        padding: 0;
        max-width: none;
    }

    iframe[title="Bản đồ chỉ đường Học viện"] {
        display: block;
        width: 100%;
        height: 100vh !important;
        height: 100dvh !important;
        min-height: 320px;
        border: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.iframe(
    Path(__file__).with_name("app.html"),
    height=900,
    alt="Bản đồ chỉ đường Học viện",
)
