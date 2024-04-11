import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from streamlit import session_state
import webbrowser


if hasattr(session_state,'login'):
    if session_state.login==True:
 


        def ValueCount(str):
            if str == "Yes":
                return 1
            else:
                return 0

        def Sex(str):
            if str == "Female":
                return 1
            else:
                return 0

        st.title(":bookmark_tabs: :blue[Autism Data Assessment]")
        st.write("---")
        st.write("Fill the form below to check if your child is suffering from ASD")

        # Load the autism dataset
        autism_dataset = pd.read_csv('asd_data_csv.csv') 

        # Separate the data and labels
        X = autism_dataset.drop(columns='Outcome', axis=1)
        Y = autism_dataset['Outcome']

        # Standardize the data
        scaler = StandardScaler()
        scaler.fit(X)
        standardized_data = scaler.transform(X)
        X = standardized_data

        # Split the data into training and testing sets
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

        # Train the SVM classifier
        classifier = svm.SVC(kernel='linear')
        classifier.fit(X_train, Y_train)

        # Form layout
        d1 = list(range(11))
        val1 = st.selectbox("Social Responsiveness", d1)

        d2 = list(range(19))
        val2 = st.selectbox("Age", d2)

        d3 = ["No", "Yes"]
        val3 = st.selectbox("Does your child look at you when you call his/her name?", d3)
        val3 = ValueCount(val3)

        val4 = st.selectbox("Can you easily establish eye contact with your child?", d3)
        val4 = ValueCount(val4)

        val5 = st.selectbox("Does your child point to indicate that she/he wants something?", d3)
        val5 = ValueCount(val5)

        val6 = st.selectbox("Does your child pretend?", d3)
        val6 = ValueCount(val6)

        val7 = st.selectbox("Does your child follow where you're looking?", d3)
        val7 = ValueCount(val7)

        val8 = st.selectbox("If you or someone else in the family is visibly upset, does your child show signs of warning to comfort them?", d3)
        val8 = ValueCount(val8)

        val9 = st.selectbox("Does your child stare at nothing with no apparent purpose?", d3)
        val9 = ValueCount(val9)

        d4 = ["Female", "Male"]
        val10 = st.selectbox("Gender", d4)
        val10 = Sex(val10)

        val11 = st.selectbox("Suffers from Jaundice", d3)
        val11 = ValueCount(val11)

        val12 = st.selectbox("Family member history with ASD", d3)
        val12 = ValueCount(val12)

        input_data = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12]

        # Reshape and standardize the input data
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        std_data = scaler.transform(input_data_reshaped)

        # Predict
        prediction = classifier.predict(std_data)

        # Display results in an expander
        with st.expander("Analyze provided data"):
            st.subheader("Results:")
            if prediction[0] == 0:
                st.info('The person is not with Autism spectrum disorder')
            else:
                st.warning('The person is with Autism spectrum disorder')

            asd_percentage = classifier.decision_function(std_data) * 100
            print("ASD Percentage:", asd_percentage)

            # Define categories and corresponding recommended video links
            categories = ["Mild", "Moderate", "Severe"]
            video_links = [
                "https://www.youtube.com/watch?v=2HNmaTdCKxM",
                "https://www.youtube.com/watch?v=DEqhWMugltk",
                "https://www.youtube.com/watch?v=PLoiHph_xwI"
            ]

            # Categorize based on ASD percentage
            if asd_percentage < 50:
                pass
            elif 50 <= asd_percentage < 75:
                st.write("Category: Mild Autism (ASD Percentage 50-75%)")
                st.write("Recommended Video Link:", video_links[0])
            elif 75 <= asd_percentage < 90:
                st.write("Category: Moderate Autism (ASD Percentage 75-90%)")
                st.write("Recommended Video Link:", video_links[1])
            else:
                st.write("Category: Severe Autism (ASD Percentage >= 90%)")
                st.write("Recommended Video Link:", video_links[2])
        def logout():
            session_state.login=False
            session_state.username=null
else:
    session_state.login=False
    webbrowser.open("http://localhost:8501/")
    st.write("please login or register")