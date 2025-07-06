# Taking info.
hours = int(input("Hours worked: "))
rate = int(input("Rate per hour: "))

# Calculating info.
income = hours * rate

# Conditions to print.
if income >= 10000:
    print("You're elite level")
elif income >= 5000:
    print("Nice side hustle")
else:
    print("Keep grinding")
