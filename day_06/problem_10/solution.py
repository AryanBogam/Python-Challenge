# Taking input of user mood.
mood = input("How are you feeling? (happy/sad/angry/motivated): ").lower()

# Conditions to print.
if mood == "happy":
    print("Keep shining")
elif mood == "sad":
    print("Go code, not cry")
elif mood == "angry":
    print("Channel that into projects")
elif mood == "motivated":
    print("This is your time to fly")
else:
    print("Unknown mood. Try again")
