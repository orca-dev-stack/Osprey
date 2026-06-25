import streamlit as st
import redis
import json
from cases.case_manager import list_cases
from utils.settings import REDIS_URL

r = redis.Redis.from_url(REDIS_URL)

st.sidebar.title("Cases")

cases = list_cases()
case_ids = [c["id"] for c in cases]
selected_case = st.sidebar.selectbox("Select case", case_ids if case_ids else ["None"])

if selected_case != "None":
    case = [c for c in cases if c["id"] == selected_case][0]

    st.subheader(f"Case: {case['id']}")
    st.markdown(f"**Severity:** {case['severity']}")
    st.markdown(f"**Status:** {case['status']}")
    st.markdown(f"**Analyst:** {case['analyst']}")
    st.markdown(f"**Message:** {case['message']}")

    st.markdown("### Timeline")
    st.markdown(f"- Created at: {case['created_at']}")
    st.markdown(f"- Last updated: {case['updated_at']}")
