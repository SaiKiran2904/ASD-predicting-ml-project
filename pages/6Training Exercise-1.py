import streamlit as st
st.title("Training Exercises")
st.title("Word Recognition Game")
st.write("Match the images to their corresponding words!")
import random
from PIL import Image
import requests
from streamlit import session_state
import webbrowser
import os

apple=os.path.abspath("image/apple4.jpg")
banana=os.path.abspath("image/banana.jpg")
cat=os.path.abspath("image/cat.jpg")
dog=os.path.abspath("image/dog.jpg")
elephant=os.path.abspath("image/elephant.jpg")
fish=os.path.abspath("image/fish.jpg")

if hasattr(session_state,'login'):
    if session_state.login==True:
     
    # Define a dictionary of words and their corresponding images
        word_image_mapping = {
            "apple":apple,
            "banana":banana,
            "cat": cat,
            "dog": dog,
            "elephant":elephant,
            "fish": fish

        # Add more word-image pairs as needed
        }

    # Function to shuffle the words
        def shuffle_words(words):
            random.shuffle(words)
            return words

    # Shuffle the words
        shuffled_words = shuffle_words(list(word_image_mapping.keys()))

    # Display the images and input boxes for word matching
        for word in shuffled_words:
            st.subheader("")  # Hiding the subheader to hide the answer
            image_path = word_image_mapping[word]
            try:
                image = Image.open(image_path)
                st.image(image, width=400, caption="")
            except Exception as e:
                st.error(f"Error loading image for {word.capitalize()}: {str(e)}")
        # Input box for user's guess
            user_guess = st.text_input("Enter your guess:", key=word.lower())

        # Check if the user's guess matches the word
            if user_guess.lower() == word.lower():
                st.success("Correct!")
            elif user_guess != "":
                st.error("Incorrect. Try again!")

# Call the display_game function
     
        

        def logout():
            session_state.login=False
            session_state.username=None
else:
    session_state.login=False
    webbrowser.open("http://localhost:8501/")


    st.write("please login or register")


