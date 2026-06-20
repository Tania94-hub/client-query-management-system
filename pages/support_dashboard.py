import streamlit as st
from query_operations import fetch_queries, close_query
import pandas as pd

st.set_page_config(page_title="Support Dashboard", layout="wide")

# Initialize session state
if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None

if st.session_state.logged_in_user is None:
    st.error("Please login first")
    st.stop()

if st.session_state.logged_in_user[3] != "Support":
    st.error("Access denied")
    st.stop()

user = st.session_state.logged_in_user
st.title(f"Support Dashboard - {user[1]}")

if st.button("Logout"):
    st.session_state.logged_in_user = None
    st.switch_page("app.py")

st.divider()

try:
    all_queries = fetch_queries()
    
    total = len(all_queries)
    open_q = len([q for q in all_queries if q[5] == "Open"])
    closed_q = len([q for q in all_queries if q[5] == "Closed"])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total", total)
    col2.metric("Open", open_q)
    col3.metric("Closed", closed_q)
    
    st.divider()
    
    status_filter = st.selectbox("Filter", ["All", "Open", "Closed"])
    
    filtered = all_queries
    if status_filter != "All":
        filtered = [q for q in all_queries if q[5] == status_filter]
    
    if filtered:
        df = pd.DataFrame(filtered, columns=["ID", "Email", "Mobile", "Heading", "Description", "Status", "Created", "Closed"])
        st.dataframe(df, use_container_width=True)
        
        st.subheader("Close Query")
        query_id = st.text_input("Enter Query ID")
        if st.button("Close"):
            if query_id:
                try:
                    close_query(query_id)
                    st.success("Closed!")
                    st.rerun()
                except:
                    st.error("Error closing")
    else:
        st.info("No queries")
except Exception as e:
    st.error(f"Error: {str(e)}")
