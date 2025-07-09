# Function to evaluate grade based on marks
def evaluate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "F"

# Get marks from user
marks = int(input("Enter marks: "))

# Display grades and marks
grade = evaluate_grade(marks)
print(f"Marks: {marks} , Grade: {grade}")