def total_subscribers(daily_subs):
    total = 0
    for subs in daily_subs:
        total += subs
    return total

daily_subs = [5, 3, 7]
result = total_subscribers(daily_subs)
print(result)

daily_subs2 = [10, 8, 12, 6, 9]
result2 = total_subscribers(daily_subs2)
print(result2)