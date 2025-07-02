# Taking info from the user.
plan = int(input("How many days you followed your plan this week (0-7)"))
hours = int(input("How many hours you studied each day (assume same daily hours): "))

cal = hours*plan

print(f"You gave your dreams {cal} hours this week -- Respect!")

if cal < 10:
    week = "Lazy week"
elif 10 <= cal < 25:
    week = "Decent week"
else: 
    week = "Elite discipline"

print(week)