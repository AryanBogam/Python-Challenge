def grade(score):
    try:
        score = int(score)
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Invalid input"

score = input("Enter score: ")
print(f"Grade: {grade(score)}")