import streamlit as st

st.set_page_config(page_title="Login State Machine", layout="centered")

VALID_USERNAME = "student"
VALID_PASSWORD = "regis123"
MAX_ATTEMPTS = 3

if "state" not in st.session_state:
    st.session_state.state = "Logged Out"

if "attempt_count" not in st.session_state:
    st.session_state.attempt_count = 0

if "message" not in st.session_state:
    st.session_state.message = "Please log in."

def login(username, password):
    if st.session_state.state == "Locked Out":
        st.session_state.message = "Account is locked. No more login attempts allowed."
        return

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        st.session_state.state = "Logged In"
        st.session_state.message = "Login successful."
        st.session_state.attempt_count = 0
    else:
        st.session_state.attempt_count += 1
        if st.session_state.attempt_count >= MAX_ATTEMPTS:
            st.session_state.state = "Locked Out"
            st.session_state.message = "Too many failed attempts. Account locked."
        else:
            st.session_state.state = "Logged Out"
            remaining = MAX_ATTEMPTS - st.session_state.attempt_count
            st.session_state.message = f"Login failed. Attempts remaining: {remaining}"

def logout():
    st.session_state.state = "Logged Out"
    st.session_state.attempt_count = 0
    st.session_state.message = "You have been logged out."

def reset_system():
    st.session_state.state = "Logged Out"
    st.session_state.attempt_count = 0
    st.session_state.message = "System reset. Please log in again."

st.title("State Transition Login App")
st.write("This sample app demonstrates State Transitions, Control Flow Testing, and Data Flow Testing.")

st.subheader("Current System State")
st.info(f"State: {st.session_state.state}")
st.write(f"Failed Attempts: {st.session_state.attempt_count}")
st.write(f"Message: {st.session_state.message}")

if st.session_state.state == "Logged In":
    st.success("Welcome! You are logged in.")
    if st.button("Logout"):
        logout()

elif st.session_state.state == "Locked Out":
    st.error("Your account is locked.")
    if st.button("Reset System"):
        reset_system()

else:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        login(username, password)

st.markdown("---")
st.subheader("Testing Notes")
st.markdown("""
- **State Transition Testing**: Check movement between Logged Out, Logged In, and Locked Out.
- **Control Flow Testing**: Check correct branch execution for success, failure, lockout, and logout.
- **Data Flow Testing**: Track how `username`, `password`, `attempt_count`, and `state` are used.
""")
