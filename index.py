import streamlit as st
import random
from PIL import Image

# Initialize session state
if 'login' not in st.session_state:
    st.session_state.login = False

# Define a dictionary of words and their corresponding images
word_image_mapping = {
    "apple": "https://cdn.pixabay.com/photo/2012/04/26/19/43/apple-42301_960_720.png",
    "banana": "https://cdn.pixabay.com/photo/2017/09/26/13/54/bananas-2788667_960_720.png",
    "cat": "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_960_720.png",
    # Add more word-image pairs as needed
}

# Function to shuffle the words and images
def shuffle_words_and_images(word_image_mapping):
    words = list(word_image_mapping.keys())
    random.shuffle(words)
    return words

# Function to display the game
def display_game():
    st.title("Word Recognition Game")
    st.write("Match the words to their corresponding images!")

    # Shuffle the words
    shuffled_words = shuffle_words_and_images(word_image_mapping)

    # Display the images and input boxes for word matching
    for word in shuffled_words:
        st.subheader(word.capitalize())
        image_url = word_image_mapping[word]
        st.image(image_url, caption=word.capitalize(), use_column_width=True)
        user_guess = st.text_input("Enter your guess:", key=word.lower())

        # Check if the user's guess matches the word
        if user_guess.lower() == word.lower():
            st.success("Correct!")
        elif user_guess != "":
            st.error("Incorrect. Try again!")

# Function to handle navigation
def main():
    st.sidebar.title("Navigation")
    if not st.session_state.login:
        st.sidebar.write("Please login to access the Word Recognition Game.")
        if st.sidebar.button("Login"):
            st.session_state.login = True
    else:
        selection = st.sidebar.radio("Go to:", ["Home", "Word Recognition Game", "Logout"])

        if selection == "Home":
            st.title("Home Page")
            st.write("Welcome to the Autism Spectrum Disorder website!")
            st.write("Please navigate to the Word Recognition Game to play.")
            # Add your home page content here

        elif selection == "Word Recognition Game":
            display_game()

        elif selection == "Logout":
            st.session_state.login = False
            st.sidebar.write("Logged out.")

if __name__ == "__main__":
    main()
