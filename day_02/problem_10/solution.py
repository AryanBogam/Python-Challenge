# Taking info from the user.
plan = int(input("How many days you followed your plan this week (0-7)"))
hours = int(input("How many hours you studied each day (assume same daily hours): "))

# Calculating hours
cal = hours*plan

# Condition to find the week.
if cal < 10:
    week = "Lazy week"
elif 10 <= cal < 25:
    week = "Decent week"
else: 
    week = "Elite discipline"

# Printing final answer.
print(f"You gave your dreams {cal} hours this week -- Respect!")
print(week)