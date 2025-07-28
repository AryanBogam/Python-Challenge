students = {"Aryan": {"math": 95, "science": 89}, "Priya": {"math": 85, "science": 92}}

name = input("Enter student name: ")
subject = input("Enter subject: ")

try:
    marks = students[name][subject]
    print(f"{name}'s {subject} marks: {marks}")
except KeyError:
    if name not in students:
        print("Student not found")
    else:
        print("Subject not found")