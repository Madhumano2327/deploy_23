import streamlit as st

# Login Credentials
login_credentials = {
    "user1": "password1",
    "user2": "password2",
}

# CareerMate Features
def career_mate_features():
    st.sidebar.header("CareerMate Features")
    feature = st.sidebar.selectbox("Choose a feature", ["Resume Builder", "Job Search", "Mentorship Program"])

    if feature == "Resume Builder":
        st.header("Resume Builder")
        st.write("Create a professional resume with our resume builder tool")
        # Resume builder code here

    elif feature == "Job Search":
        st.header("Job Search")
        st.write("Find job opportunities that match your skills and interests")
        # Job search code here

    elif feature == "Mentorship Program":
        st.header("Mentorship Program")
        st.write("Get guidance and support from experienced professionals in your industry")
        # Mentorship program code here

# Login Page
def login_page():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in login_credentials and login_credentials[username] == password:
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")

# Streamlit App
def main():
    st.title("CareerMate")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login_page()
    else:
        career_mate_features()

