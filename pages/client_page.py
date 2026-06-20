import streamlit as st
from query_operations import fetch_queries, insert_query, close_query
import pandas as pd
import uuid

st.set_page_config(page_title="Client Dashboard", layout="wide")

# Initialize session state
if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None

if st.session_state.logged_in_user is None:
    st.error("Please login first")
    st.stop()

if st.session_state.logged_in_user[3] != "Client":
    st.error("Access denied")
    st.stop()

user = st.session_state.logged_in_user
username = user[1]

st.title(f"Welcome {username}")

if st.button("Logout"):
    st.session_state.logged_in_user = None
    st.switch_page("app.py")

st.divider()

tab1, tab2 = st.tabs(["Submit Query", "My Queries"])

with tab1:
    st.subheader("Submit New Query")
    
    mail_id = st.text_input("Email")
    mobile = st.text_input("Mobile Number")
    heading = st.text_input("Query Heading")
    description = st.text_area("Description")
    
    if st.button("Submit"):
        if all([mail_id, mobile, heading, description]):
            try:
                query_id = f"Q{str(uuid.uuid4())[:8]}"
                insert_query(query_id, mail_id, mobile, heading, description)
                st.success("Query submitted!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
