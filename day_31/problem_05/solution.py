students = [(101, "Alice", 95), (102, "Bob", 78), (103, "Charlie", 45), (104, "Diana", 88)]

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

print("STUDENT RESULT CARD")
print("=" * 50)
print("Roll No".ljust(10) + "Name".ljust(15) + "Marks".ljust(10) + "Grade")
print("-" * 50)

for roll_no, name, marks in students:
    grade = get_grade(marks)
    print(str(roll_no).ljust(10) + name.ljust(15) + str(marks).ljust(10) + grade)

print("=" * 50)