import streamlit as st

# Function to convert marks to grade points
def marks_to_grade(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    else:
        return 0

st.title("CGPA Calculator")

n = st.number_input("Enter number of subjects", min_value=1, step=1)

total_credit_points = 0
total_credits = 0

for i in range(int(n)):
    st.subheader(f"Subject {i+1}")
    
    marks = st.number_input(f"Marks for Subject {i+1}", key=f"marks_{i}")
    credits = st.number_input(f"Credits for Subject {i+1}", key=f"credits_{i}")
    
    grade_point = marks_to_grade(marks)
    credit_points = grade_point * credits
    
    total_credit_points += credit_points
    total_credits += credits

if st.button("Calculate CGPA"):
    if total_credits > 0:
        cgpa = total_credit_points / total_credits
        st.success(f"Your CGPA is: {round(cgpa, 2)}")
    else:
        st.error("Please enter valid credits!")
        
        
# Here is the website link
# https://calculate-cgpa-points.streamlit.app/