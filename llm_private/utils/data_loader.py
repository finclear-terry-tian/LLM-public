import streamlit as st
import os
import pandas as pd


@st.cache_data
def get_client_inscope():
    path = os.path.join(st.session_state['root_path'], 'data', 'inscope.csv')
    df = pd.read_csv(path)
    df = df.head(10000)
    return df


@st.cache_data
def get_client_portfolio():
    path = os.path.join(st.session_state['root_path'], 'data', 'portfolio.csv')
    df = pd.read_csv(path, parse_dates=['Date'])
    return df


