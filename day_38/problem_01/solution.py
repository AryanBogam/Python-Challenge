def check_streak(days):
    if days >= 3:
        return "Streak Active!"
    elif days == 0:
        return "Streak Lost"
    else:
        return "Keep Snapping!"
    
result = check_streak(5)
print(result)

result2 = check_streak(0)
print(result2)

result3 = check_streak(2)
print(result3)