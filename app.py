import streamlit as st
from auth import register_user, login_user

# Initialize session state
if 'logged_in_user' not in st.session_state:
    st.session_state.logged_in_user = None

st.set_page_config(
    page_title="Client Query Management System",
    layout="centered"
)

st.title("Client Query Management System")

# Only show login/register if NOT logged in
if st.session_state.logged_in_user is None:
    
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        st.subheader("Create New Account")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        role = st.selectbox("Select Role", ["Client", "Support"])

        if st.button("Register"):
            try:
                register_user(new_username, new_password, role)
                st.success("User Registered Successfully. Now login!")
            except:
                st.error("Username already exists")

    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state.logged_in_user = user
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

# If logged in, redirect to appropriate page
else:
    user = st.session_state.logged_in_user
    role = user[3]
    
    if role == "Client":
        st.switch_page("pages/client_page.py")
    elif role == "Support":
        st.switch_page("pages/support_dashboard.py")
