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