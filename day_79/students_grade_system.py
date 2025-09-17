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

# Function to update a student's grade
def update_student(name, grade):
    # Check if student exists in dictionary
    if name in student_grades:
        # Update the student's grade
        student_grades[name] = grade
        #Sagar = 200
        # Print update confirmation
        print(f"{name} with marks are updated {grade}")
    else:
        # Print error if student not found
        print(f"{name} is not found!")

# Function to delete a student
def delete_student(name):
    # Check if student exists in dictionary
    if name in student_grades:
        # Remove student from dictionary
        del student_grades[name]
        # Print deletion confirmation
        print(f"{name} has been successfully deleted")
    else:
        # Print error if student not found
        print(f"{name} is not found!")


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

# Main function to run the program
def main():
    # Start infinite loop for menu
    while True:
        # Display menu options
        print("\n Student Grades Management System")
        print("1. Add student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        # Get user's choice
        choice = int(input("enter your choice = "))

        # Add student option
        if choice == 1:
            # Get student name from user
            name = input("Enter student name = ")
            # Get student grade from user
            grade = int(input("Enter student grade = "))
            # Call add_student function
            add_student(name,grade)

        # Update student option
        elif choice == 2:
            # Get student name to update
            name = input("Enter student name = ")
            # Get new grade
            grade = int(input("Enter student grade = "))
            # Call update_student function
            update_student(name, grade)

        # Delete student option
        elif choice == 3:
            # Get student name to delete
            name = input("Enter student name = ")
            # Call delete_student function
            delete_student(name)

        # View all students option
        elif choice == 4:
            # Call display_all_students function
            display_all_students()

        # Exit option
        elif choice == 5:
            # Print exit message and break loop
            print("Closing the program...")
            break
        
        # Handle invalid choices
        else:
            print("Invalid choice, Select between 1 to 5")

# Run the main function
main()