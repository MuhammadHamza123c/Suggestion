import firebase_admin
import streamlit as st
from firebase_admin import credentials, db
import json
import os

# Load Firebase credentials from Streamlit Secrets
firebase_secrets = st.secrets["firebase"]
cred = credentials.Certificate(firebase_secrets)

# Initialize Firebase app only once
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://suggestion-d9014-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

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
