# Initialising dictionary to store student names and grades
student_grades = { }


# Function to add a new student
def add_student(name, grade):
    # Store student name and grade in dictionary
    student_grades[name] = grade
    # [sagar] = 100
    # Print confirmation message
    print(f"Added {name} with a {grade}")
    # Added sagar with a 100


# Function to view all students and their grades
def display_all_students():
    # Check if dictionary has any students
    if student_grades:
        # Loop through all students in dictionary
        for name, grade in student_grades.items():
            # Print each student's name and grade
            print(f"{name} : {grade}")
    else:
        # Print message if no students found
        print("No students found/Added")