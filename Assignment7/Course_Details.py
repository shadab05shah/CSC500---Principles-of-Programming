""""
Assignment 7
Course Details
Author: Shadab
"""

# Python code using Dictionaries to store Course Details
# user provides Inputs at Runtime and also validations for inputs

room_numbers = {
    "CSC101" : "3004",
    "CSC102" : "4501",
    "CSC103" : "6755",
    "NET110" : "1244",
    "COM241" : "1411"
}

instructors = {
    "CSC101" : "Haynes",
    "CSC102" : "Alvarado",
    "CSC103" : "Rich",
    "NET110" : "Burke",
    "COM241" : "Lee"
}

meeting_times = {
    "CSC101" : "8:00 a.m.",
    "CSC102" : "9:00 a.m.",
    "CSC103" : "10:00 a.m.",
    "NET110" : "11:00 a.m.",
    "COM241" : "1:00 p.m."
}

# Input Validation
while True:
    course_code = input("Enter course number: ").strip().upper()

    if course_code == "":
        print("Warning!! Input cannot be empty. Input valid value.")
        continue

    if not (course_code[:3].isalpha() and course_code[3:].isdigit()):
        print("Warning!! Invalid course code format. Input a valid course code format like CSC101.")
        continue

    if course_code not in room_numbers:
        print("Course not found. Input a valid course code.")
        continue

    break

# Display Results
print("\n************ Course Details *************\n")
print("Course Number Entered:", course_code)
print("Room Number:", room_numbers[course_code])
print("Instructor:", instructors[course_code])
print("Meeting Time:", meeting_times[course_code])
print('\n*****************************************\n')