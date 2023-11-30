#LinkedIn API


#Installation of required packages
pip install streamlit
pip install requests
pip install requests_oauthlib
pip install oauthlib

#Import of required packages
import streamlit as st
import requests
from requests_oauthlib import OAuth2Session
from urllib.parse import urlparse, parse_qs

# Constants
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:8501'  # This should match your Streamlit app's address
AUTHORIZATION_BASE_URL = 'https://www.linkedin.com/oauth/v2/authorization'
TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
SCOPE = ['r_liteprofile']  # Define your scopes here
