import streamlit as st
import sqlite3
from streamlit import session_state
import webbrowser
from datetime import datetime

# Function to create a SQLite connection
def create_connection():
    return sqlite3.connect("contact_form_data.db")  # Adjust the database name as needed

# Create the "contacts" table if it doesn't exist
def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            dob TEXT,
            gender TEXT,
            message TEXT,
            approved INTEGER DEFAULT 0
        )
    ''')
    connection.commit()
    connection.close()

# Function to insert contact form data into the database
def insert_contact_data(name, email, phone, dob, gender, message):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO contacts (name, email, phone, dob, gender, message) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, email, phone, dob, gender, message))
    connection.commit()
    connection.close()

if hasattr(session_state, 'login') and session_state.login:
    st.title(":mailbox: :blue[Get In Touch With Us!]")
    
    # Create the contacts table
    create_table()

    # Get form input
    name = st.text_input("Your name:", key="name")
    email = st.text_input("Your email:", key="email")
    phone = st.text_input("Your phone number:", key="phone")
    
    # Set date range from 1950 to the current year
    max_year = datetime.now().year
    min_date = datetime(1950, 1, 1)
    max_date = datetime(max_year, 12, 31)
    dob = st.date_input("Your date of birth:", key="dob", min_value=min_date, max_value=max_date)
    
    gender = st.selectbox("Your gender:", ["Male", "Female", "Other"], key="gender")
    message = st.text_area("Your message:", key="message")

    if st.button("Submit"):
        # Insert data into the database
        insert_contact_data(name, email, phone, dob, gender, message)
        st.success("Your message has been submitted for admin approval.")

    # Logout button
    if st.button("Logout"):
        session_state.login = False
        session_state.username = None

else:
    session_state.login = False
    webbrowser.open("http://localhost:8501/")
    st.write("Please login or register")
