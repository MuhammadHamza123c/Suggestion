import firebase_admin
import streamlit as st
from firebase_admin import credentials, db

# ✅ Ensure Firebase is initialized only once
if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\HP\Downloads\suggestion-d9014-firebase-adminsdk-fbsvc-a142dfcb5f.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://suggestion-d9014-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })

# ✅ Firebase Database Reference
suggestion = db.reference('/Suggestion')

# ✅ Streamlit UI
st.title("Firebase + Streamlit App")

user_name = st.text_input("Write down your name:")
user_age = st.number_input("Write down your age:", min_value=1, max_value=120, step=1)
sugges = st.text_input("Write down your suggestion:")

if st.button("Submit"):
    if user_name and user_age and sugges:
        suggestion.push({
            'Name': user_name,
            'Age': user_age,
            'Suggestion': sugges
        })
        st.success("✅ Data saved to Firebase!")
    else:
        st.warning("⚠️ Please fill all fields before submitting.")
