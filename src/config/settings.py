import streamlit as st

def initialize_session_state():
    """Initialize session state variables."""
    if 'mode' not in st.session_state:
        st.session_state.mode = "Learning Path"
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    if 'groq_api_key' not in st.session_state:
        st.session_state.groq_api_key = ""
    if 'serpapi_api_key' not in st.session_state:
        st.session_state.serpapi_api_key = ""
    if 'openai_api_key' not in st.session_state:
        st.session_state.openai_api_key = ""
    if 'firecrawl_api_key' not in st.session_state:
        st.session_state.firecrawl_api_key = "" 