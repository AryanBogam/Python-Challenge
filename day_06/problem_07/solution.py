# Taking info.
study_hours = float(input("Study hours today: "))
screen_hours = float(input("Screen time (non-productive): "))


# Condition to print.
if study_hours > screen_hours:
    print("Discipline")
else:
    print("You're losing to your habits")
