import os
import pandas as pd
import streamlit as st
st.header ("Secure Student Portal and Academic Information System ")
st.title("Student Portal Login")
username = st.text_input("Enter username: ", key="main_user")
if username == "@Enoch1234":
    st.write("Username is correct!")
elif username != "":
    st.write("Wrong username! Try again.")
password = st.text_input("Enter password: ", type="password", key="main_pass")
if username == "@Enoch1234" and password == "Enoch123":
    st.success("Login Successfully!")
    st.write("-" * 40)
    menu = st.sidebar.selectbox(
        "Choose Menu",
        ["Home", "Secure Student Portal", "Enter Student Name and Marks", "About", "Contact", "Comments"]
    )
    class StudentIntroduction:
        def __init__(self, name, age, roll_no, dateofbirth, department, placefrom, clubmember, college_name):
            self.name = name
            self.age = age
            self.roll_no = roll_no
            self.dateofbirth = dateofbirth
            self.department = department
            self.placefrom = placefrom
            self.clubmember = clubmember
            self.college_name = college_name
        def display(self):
            st.write("Name:", self.name)
            st.write("Age:", self.age)
            st.write("Date of Birth:", self.dateofbirth)
            st.write("Rollno:", self.roll_no)
            st.write("Place from:", self.placefrom)
            st.write("Department:", self.department)
            st.write("Club member:", self.clubmember)
            st.write("College name:", self.college_name)
    class StudentMarks:
        def __init__(self, tamil, english, maths, c_programming, computer_fundamental, vac):
            self.tamil = tamil
            self.english = english
            self.maths = maths
            self.c_programming = c_programming
            self.computer_fundamental = computer_fundamental
            self.vac = vac
        def display(self):
            st.write("Tamil:", self.tamil)
            st.write("English:", self.english)
            st.write("Maths:", self.maths)
            st.write("C programming:", self.c_programming)
            st.write("Computer Fundamental:", self.computer_fundamental)
            st.write("VAC:", self.vac)
        def get_total(self):
            return self.tamil + self.english + self.maths + self.c_programming + self.computer_fundamental + self.vac
        def get_average(self):
            return self.get_total() / 6
        def check_status(self):
            return "Pass" if min([
                self.tamil, self.english, self.maths,
                self.c_programming, self.computer_fundamental, self.vac
            ]) >= 40 else "Fail"
    if menu == "Home":
        st.write("Welcome to the Home page")
        st.title("Student Portal")
        st.write("Good morning Everyone!")
        st.write("-" * 40)
    elif menu == "Secure Student Portal":
        st.header("Secure Student Portal Verification")
        st.write("Please verify your credentials again to view private student records.")
        sec_password = st.text_input("Enter password: ", type="password", key="sec_pass")
        if  sec_password == "Enoch456":
            st.success("Access Granted to Student Record!")
            st.write("-" * 40)
            S1 = StudentIntroduction(
                "Enoch Andrew Jaisingh", 19, 14, "7-10-2007",
                "BCA 1st year", "Mangadu", "Data Science", "St Joseph_university"
            )
            S1.display()
            st.write("-" * 40)
            S2 = StudentMarks(100, 100, 100, 100, 100, 100)
            S2.display()
            st.write("-" * 40)
            st.write("Total Marks obtained:", S2.get_total())
            st.write("Average Marks:", round(S2.get_average(), 2))
            st.write("Academic Status:", S2.check_status())
        elif sec_password != "":
            st.error("Wrong password! Access denied.")
    elif menu == "Enter Student Name and Marks":
        st.title("Student Marks Calculator & Graph")
        name = st.text_input("Enter your name:")
        st.write("Enter your marks below:")
        tamil = st.number_input("Enter your Tamil marks:", 0, 100, value=0)
        english = st.number_input("Enter your English marks:", 0, 100, value=0)
        maths = st.number_input("Enter your Maths marks:", 0, 100, value=0)
        c_programming = st.number_input("Enter your C programming marks:", 0, 100, value=0)
        computer_fundamental = st.number_input("Enter your Computer Fundamental marks:", 0, 100, value=0)
        vac = st.number_input("Enter your VAC marks:", 0, 100, value=0)
        custom_marks = StudentMarks(tamil, english, maths, c_programming, computer_fundamental, vac)
        st.write("-" * 40)
        if name:
            st.write(f"**Student Name:** {name}")
        st.write("**Total Marks:**", custom_marks.get_total())
        st.write("**Average Marks:**", round(custom_marks.get_average(), 2))
        st.write("**Status:**", custom_marks.check_status())
        chart_data = pd.DataFrame({
            "Marks": [tamil, english, maths, c_programming, computer_fundamental, vac]
        }, index=["Tamil", "English", "Maths", "C Programming", "Computer Fundamental", "VAC"])
        st.bar_chart(chart_data)
    
elif page == "About":
    st.title("About Us")

    st.subheader("Secure Student Portal and Academic Information System")

    st.subheader"""
     What is a Secure Student Portal and Academic Information System?

    It is a web-based application developed using Python
    and Streamlit to manage and display student information.

     Why Do We Call It This Name?

    1. Secure: Because it uses password protection to
    restrict access to student information.

    2.Student Portal: Because students can view their
    personal details and academic information.

    3.Academic Information System: Because it manages
    subject marks, calculates total and average marks,
    checks Pass or Fail results, and displays marks
    through a bar chart.

     4.Main Purpose

    The main purpose of this project is to provide a
    simple and organized way to view student details
    and perform academic mark calculations.

    5.Technologies Used
    - Python
    - Streamlit
    - Pandas



    
    create by: Enoch Andrew Jaisingh 
    department: BCA 1styear 
    Club member: DataScience
    """)

    elif menu == "Contact":
        st.header("Contact")
        st.write("Email: enochandrewjaisingh2007@gmail.com")
    elif menu == "Comments":
        st.header("Comments")
        comments = st.text_input("Leave your comments here:")
        checkbox = st.checkbox("I agree to the terms and conditions.")
        if checkbox:
            st.write("Thank you for agreeing to the terms and conditions.")
st.write("-" * 40)
st.subheader("Saved Comments")
if os.path.exists("comments.csv"):
            comments_df = pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\my project\comments.csv")
            st.dataframe(comments_df)
