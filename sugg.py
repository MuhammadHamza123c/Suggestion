import firebase_admin
import streamlit as st
from firebase_admin import credentials, db
import json

# Load Firebase credentials from Streamlit Secrets
firebase_secrets = st.secrets["firebase"]

# Convert private_key to a properly formatted string
firebase_secrets_dict = {
    "type": firebase_secrets["type"],
    "project_id": firebase_secrets["project_id"],
    "private_key_id": firebase_secrets["private_key_id"],
    "private_key": firebase_secrets["private_key"].replace('\\n', '\n'),  # Fix newline issue
    "client_email": firebase_secrets["client_email"],
    "client_id": firebase_secrets["client_id"],
    "auth_uri": firebase_secrets["auth_uri"],
    "token_uri": firebase_secrets["token_uri"],
    "auth_provider_x509_cert_url": firebase_secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": firebase_secrets["client_x509_cert_url"]
}

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_secrets_dict)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://suggestion-d9014-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# Reference to Firebase Database
suggestion = db.reference('/Suggestion')

# Streamlit UI
user_name = st.text_input("Write down name here:")
if user_name:
    user_age = st.number_input("Write down age here:", min_value=1, max_value=100)
    if user_age:
        sugges = st.text_input("Write down suggestion here:")
        if sugges:
            suggestion.push({
                'Name': user_name,
                'Age': user_age,
                'Suggestion': sugges
            })
            st.success("Data submitted successfully!")
