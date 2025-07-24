students = {
    "Alice": [85, 92, 78, 90],
    "Bob": [76, 81, 85, 79],
    "Charlie": [95, 98, 92, 94],
    "Diana": [88, 85, 91, 87]
}

print("Student Averages:")
for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(f"{name}: {avg}")

top_student = ""
highest_avg = 0

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print(f"Top Scorer: {top_student} with average {highest_avg}")