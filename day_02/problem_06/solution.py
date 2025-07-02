# Taking info from the user.
age = int(input("Enter your age: "))
retire = int(input("At what age you what to retire: "))
hours = int(input("Daily learning hours: "))

# Calculating the remaining days to retire.
years_r = (retire-age)*365

# Calculating the hours remaining to retire.
hours_r = hours*years_r

# Printing final answer.
print(f"You have {years_r} days and {hours_r} hours left to learn before your dream life.")