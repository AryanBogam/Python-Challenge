
students = (("Aryan", 89), ("Riya", 92), ("Om", 76))

# Top scorer
topper = max(students, key=lambda x: x[1])  # Use lambda to access marks

# Average score
total = sum([score for name, score in students])
average = total / len(students)

# Total students
total_students = len(students)

# Final Answer.
print(" Topper:", topper[0], "with", topper[1], "marks")
print(" Average Score:", average)
print(" Total Students:", total_students)
