# Taking info.
total = int(input("Total course hours: "))
done = int(input("Hours completed: "))

# Calculating percentage.
percent = (done / total) * 100


# Conditions to print.
if percent == 100:
    print("You crushed it")
elif percent >= 75:
    print("Almost there")
elif percent < 50 and percent > 0:
    print("Get serious")
else:
    print("Why did you even start?")
