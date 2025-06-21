import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agent.agent_core import run_research_and_summarize

st.set_page_config(page_title="AI Research & Summarizer Agent")

st.title("AI Research & Summarizer Agent")
query = st.text_input("Enter your research topic or question:")

if st.button("Run Research"):
    with st.spinner("Agent is researching..."):
        summary, links = run_research_and_summarize(query)
        st.subheader("Summary")
        st.write(summary)
        st.subheader("Sources")
        for url in links:
            st.write(url)
