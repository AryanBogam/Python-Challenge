students = {
    "Aryan": ["Python", "Math", "AI"],
    "Riya": ["Math", "Physics"],
    "Om": ["Python"]
}

print("Student Course List:")
for name, courses in students.items():
    print(f"{name}: {', '.join(courses)}")

search_course = input("\nEnter a course to search: ")

print(f"\nStudents enrolled in {search_course}:")
found = False
for name, courses in students.items():
    if search_course in courses:
        print(f"- {name}")
        found = True

if not found:
    print("No students enrolled in this course.")
