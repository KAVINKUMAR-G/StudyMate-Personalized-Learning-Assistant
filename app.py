
import streamlit as st

st.set_page_config(page_title="StudyMate", page_icon="📘")

st.title("📘 StudyMate")
st.subheader("Personalized Learning Assistant")

st.write("Welcome! Let's create your personal study plan.")

name = st.text_input("Enter your name")

subject = st.selectbox(
    "Choose your subject",
    ["Python", "Machine Learning", "Data Structures"]
)

level = st.selectbox(
    "Select your learning level",
    ["Beginner", "Intermediate", "Advanced"]
)

hours = st.number_input(
    "Available study time (hours)",
    min_value=1,
    max_value=10,
    value=2
)

if st.button("Generate Study Plan"):
    if name.strip():
        st.success(f"Welcome {name}!")

        st.subheader("Your Personalized Study Plan")

        topics = {
            "Python": ["Variables", "Loops", "Functions"],
            "Machine Learning": ["Introduction to ML", "Data Preprocessing", "Model Training"],
            "Data Structures": ["Arrays", "Stacks and Queues", "Trees"]
        }

        st.write(f"**Subject:** {subject}")
        st.write(f"**Level:** {level}")
        st.write(f"**Study Time:** {hours} hours")

        for i, topic in enumerate(topics[subject], 1):
            st.write(f"{i}. {topic}")

        st.balloons()
    else:
        st.warning("Please enter your name.")
