def display_daily_messages(daily_counts):
    for day in daily_counts:
        count = daily_counts[day]
        print(f"{day}: {count}")

daily_counts = {
    "Mon": 45,
    "Tue": 60,
    "Wed": 30,
    "Thu": 55,
    "Fri": 70,
    "Sat": 25,
    "Sun": 40
}

display_daily_messages(daily_counts)
def get_weekly_total(daily_counts):
    total = 0
    for day in daily_counts:
        total += daily_counts[day]
    return f"Weekly total: {total} messages"

result = get_weekly_total(daily_counts)
print(result)