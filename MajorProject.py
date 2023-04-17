import streamlit as st

# Page title
st.title("BMI Calculator")

# Name input
name = st.text_input("Name")

# Gender input
gender = st.radio("Gender", options=["Male", "Female", "Other"])

# Age input
age = st.number_input("Age", min_value=1, max_value=150, step=1)

# Address input
address = st.text_input("Address")

# Hobbies input
hobbies = st.multiselect("Hobbies", options=["Playing", "Reading", "Singing"])

# Weight input
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=500.0, step=0.1)

# Height input
height = st.number_input("Height (cm)", min_value=1, max_value=300, step=1)

# Calculate BMI
if st.button("Calculate BMI"):
    # BMI calculation
    height_m = height / 100 # Convert height to meters
    bmi = weight / (height_m * height_m) # BMI formula
    st.write("Your BMI: {:.2f}".format(bmi))

