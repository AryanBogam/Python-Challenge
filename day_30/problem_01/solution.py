students = [("Aryan", 88), ("Riya", 94), ("Kabir", 75), ("Sara", 94)]

highest_marks = 0
for name, marks in students:
    if marks > highest_marks:
        highest_marks = marks

toppers = []
for name, marks in students:
    if marks == highest_marks:
        toppers.append(name)

print(f"Highest marks: {highest_marks}")
print(f"Toppers: {toppers}")