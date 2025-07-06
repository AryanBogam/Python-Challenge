# Taking info.
gpa = float(input("Enter your GPA (out of 10): "))
projects = int(input("Number of GitHub projects: "))


# Conditions to print.
if gpa >= 9 or projects >= 5:
    print("Strong Candidate!")
elif gpa >= 8:
    print("Improve your GitHub portfolio.")
else:
    print("Work harder on both academics and projects.")
