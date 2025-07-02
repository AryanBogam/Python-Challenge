# Taking info from the user.
mood = input("Enter your mood eg.(lazy/curious/focused)")
topic = input("Enter your favorite topic eg.(AI/Math/Business)")

# Conditions for printing.
if mood == "lazy":
    print(f"Watch Youtube shorts on {topic}")
elif mood == "curious":
    print(f"Read 1 blog on {topic}")
else:
    print(f"do 2-hours deep work on {topic}")