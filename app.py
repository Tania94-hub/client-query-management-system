import streamlit as st
from auth import register_user, login_user

st.set_page_config(
    page_title="Client Query Management System",
    layout="centered"
)

st.title("Client Query Management System")

menu = ["Login", "Register"]

choice = st.sidebar.selectbox("Menu", menu)

# ---------------- REGISTER ---------------- #

if choice == "Register":

    st.subheader("Create New Account")

    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    role = st.selectbox(
        "Select Role",
        ["Client", "Support"]
    )

    if st.button("Register"):

        try:
            register_user(
                new_username,
                new_password,
                role
            )

            st.success("User Registered Successfully")

        except:
            st.error("Username already exists")


# ---------------- LOGIN ---------------- #

elif choice == "Login":

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = login_user(username, password)

        if user:

            st.success("Login Successful")

            st.write("Welcome:", user[1])
            st.write("Role:", user[3])

            # Redirect logic
            if user[3] == "Client":
                st.info("Go to Client Page")

            elif user[3] == "Support":
                st.info("Go to Support Dashboard")

        else:
            st.error("Invalid Username or Password")