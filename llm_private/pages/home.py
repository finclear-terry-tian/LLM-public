import streamlit as st

def app():

    # Configure page
    page = 'home'
    st.title(f'{st.session_state.app.pages[page].icon} {st.session_state.app.pages[page].title}')
    st.header("Welcome to FinClear's llm! 👋")
