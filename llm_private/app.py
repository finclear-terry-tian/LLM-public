import streamlit as st
import streamlit_authenticator as stauth
import os
import PIL
from .utils.multipage import MultiPage

def build_app():

    # Import all pages here for cleaner dependency handling
    from .pages import home

    app = MultiPage()
    app.add_page('home', 'Home', '🏠', home.app)


    # Load images
    if 'root_path' not in st.session_state:
        st.session_state['root_path'] = os.path.dirname(__file__)

    if 'images' not in st.session_state:
        st.session_state['images'] = {}

    if 'logo' not in st.session_state.images:
        logo_path = os.path.join(st.session_state['root_path'], 'images', 'logo_tagline.png')
        st.session_state.images['logo'] = PIL.Image.open(logo_path)

    if 'letter_b' not in st.session_state.images:
        lb_path = os.path.join(st.session_state['root_path'], 'images', 'letter_b.png')
        st.session_state.images['letter_b'] = PIL.Image.open(lb_path)

    if 'letter_s' not in st.session_state.images:
        ls_path = os.path.join(st.session_state['root_path'], 'images', 'letter_s.png')
        st.session_state.images['letter_s'] = PIL.Image.open(ls_path)

    return app


def load_secrets():

    # Authentication
    credentials = dict(st.secrets.auth.credentials)  # Must copy this as it is modified by stauth
    cookie = st.secrets.auth.cookie
    preauthorised = st.secrets.auth.preauthorised

    if 'authenticator' not in st.session_state:
        st.session_state['authenticator'] = stauth.Authenticate(
            credentials, cookie.name, cookie.key, int(cookie.expiry_days), preauthorised)

    # if 'openai_api_key' not in st.session_state:
    #     st.session_state['openai_api_key'] = st.secrets.api_keys.openai


def authenticate():
    """
    This is the main app function called from the module by the public repo
    """

    # Load secrets
    load_secrets()

    # Run authentication window
    st.session_state.authenticator.login('Login')

    # Control flow of authentication
    if st.session_state['authentication_status']:

        # Build app on login
        if 'app' not in st.session_state:
            st.session_state['app'] = build_app()

        st.session_state.app.run()

    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')

    elif st.session_state["authentication_status"] == None:
        st.info('Please enter your username and password')

        # Reset app when logout
        if 'app' in st.session_state:
            del st.session_state['app']
