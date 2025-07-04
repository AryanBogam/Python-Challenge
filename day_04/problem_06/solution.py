# Given.
python_students = {"Aryan", "Riya", "Om", "Tina"}
ai_students = {"Riya", "Tina", "Sahil"}
all_students = {"Aryan", "Riya", "Om", "Tina", "Sahil", "Meera"}

# Students who completed both
both_courses = python_students & ai_students  

# Students who completed only one 
only_one_course = python_students ^ ai_students  

# Students who completed none
completed_any = python_students | ai_students  
none_completed = all_students - completed_any

print("Completed both Python & AI:", both_courses)
print("Completed only one course:", only_one_course)
print("Completed none:", none_completed)
