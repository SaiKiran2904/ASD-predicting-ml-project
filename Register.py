import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import time
import requests
from streamlit_lottie import st_lottie
from streamlit import session_state
import base64



# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def validate_input(username, password):
    if not username or not password:
        st.warning("Please provide both username and password.")
        return False
    elif len(username) < 6 or len(password) < 6:
        st.warning("Username and password must be at least 6 characters long.")
        return False
    return True

with st.sidebar:
    selected=option_menu(
        menu_title="ASD Prediction!",
        options=["Signup","Login"],
        icons=["box-seam-fill","box-seam-fill"],
        menu_icon="home",
        default_index=0
    )
def logout():
    delattr(session_state,'login')

if selected=="Signup" :

    st.title(":iphone: :blue[Create New Account]")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')
    if new_user!='' and new_password!='':
        if len(new_user)>5 and len(new_password)>5:
            if new_user.isalnum() and new_password.isalnum():
                if st.button("Signup"):
                    create_usertable()
                    add_userdata(new_user,new_password)
                    st.success("You have successfully created a valid Account")
                    st.info("Go to Login Menu to login")
                else:
                     st.warning("please include both alphabets and numbers")
        else:
            st.warning("please enter min 6 characters ")
    else:
        st.warning("please enter username and password")

elif selected=="Login" :
    st.title(":calling: :blue[Login Section]")
    username = st.text_input("User Name")
    password = st.text_input("Password",type='password')
    if username!='' and password!='':
            if st.button("Login"):
                create_usertable()
      
                result = login_user(username,password)
       
                if result:
                    st.success("Logged In as {}".format(username))
                    session_state.login=True
                    session_state.username=username
                    st.warning("Go to Dashboard!")
                else:
                    st.warning("Incorrect Username/Password")
        
if hasattr(session_state,'login'):
    if st.button("Logout"):
        logout()
        st.success("You have been logged out.")
