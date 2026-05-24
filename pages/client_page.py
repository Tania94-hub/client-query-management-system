import streamlit as st
from query_operations import insert_query
from datetime import datetime

st.title("Client Query Submission Page")

st.subheader("Submit Your Query")

# Input fields
mail_id = st.text_input("Email ID")

mobile_number = st.text_input("Mobile Number")

query_heading = st.text_input("Query Heading")

query_description = st.text_area("Query Description")


# Generate Query ID
query_id = "Q" + datetime.now().strftime("%H%M%S")


# Submit button
if st.button("Submit Query"):

    insert_query(
        query_id,
        mail_id,
        mobile_number,
        query_heading,
        query_description
    )

    st.success("Query Submitted Successfully")

    st.write("Generated Query ID:", query_id)