# The given student IDs.
student_IDs = [101, 102, 103, 101, 104, 102, 105]

# Converting the list into set.
unique_IDs = set(student_IDs)

# Finding the multiple students.
multiple_students = len(student_IDs) - len(unique_IDs)

# Printing the final answer.
print(f"{multiple_students} students were counted multiple times.")
