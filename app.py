import streamlit as st
import time
import random

# Set page configuration
st.set_page_config(page_title="Python Developer Quiz", page_icon="🐍", layout="wide")

# Python Developer Quiz Questions
questions = [
    {"question": "What is the output of 3 + 2 * 2 in Python?", "options": ["5", "7", "10", "8"], "answer": "7"},
    {"question": "What is the correct syntax for defining a function in Python?", "options": ["def function()", "function def()", "def function[]", "function():"], "answer": "def function()"},
    {"question": "Which of the following is a mutable data type in Python?", "options": ["list", "tuple", "string", "int"], "answer": "list"},
    {"question": "What does 'self' represent in a Python class?", "options": ["The instance of the class", "The class itself", "The parent class", "The method of the class"], "answer": "The instance of the class"},
    {"question": "How do you declare a variable in Python?", "options": ["variable = 5", "int variable = 5", "var 5 = int", "var 5 = 5"], "answer": "variable = 5"}
]

# Shuffle questions for randomness
random.shuffle(questions)

# App title and description
st.title("🐍 Python Developer Quiz Challenge 🐍")
st.markdown("Welcome to the Python Developer Quiz! Test your Python programming skills and see how well you know Python!")

# Styling for the quiz interface
st.markdown("""
    <style>
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            padding: 12px 24px;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .stRadio > div {
            font-size: 18px;
        }
        .stMarkdown {
            font-size: 20px;
            color: #333;
        }
        .stTextInput input {
            font-size: 20px;
            padding: 10px;
        }
        .stAlert {
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)

# Timer Function
def timer(duration):
    with st.empty():
        for i in range(duration, 0, -1):
            st.markdown(f"**Time Left: {i} seconds**")
            time.sleep(1)
        st.markdown("**Time's up!**")

# Function to display each question and options
def display_question(q):
    st.subheader(q['question'])
    answer = st.radio("Select your answer:", q['options'], index=0)
    return answer

# Quiz Logic
def run_quiz():
    score = 0
    question_number = 1

    # Loop through all questions
    for q in questions:
        st.markdown(f"### Question {question_number}")
        st.markdown("### ⏳ You have 10 seconds to answer this question!")
        
        # Start Timer
        timer(10)

        # Display the question and get user's answer
        user_answer = display_question(q)
        correct_answer = q['answer']
        
        # Check answer and provide feedback
        if user_answer == correct_answer:
            score += 1
            st.success("Correct Answer! 🎉")
        else:
            st.error(f"Incorrect Answer! The correct answer was: {correct_answer} ❌")

        question_number += 1

    # Display final score
    st.markdown(f"### Your Final Score: {score}/{len(questions)}")
    st.markdown("### Thank you for taking the quiz! Well Done! 👏")

# Start quiz button
if st.button("Start Quiz"):
    run_quiz()
