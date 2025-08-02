def convert_to_24hr(time_str):
    words = time_str.split()

    time_part = None
    for word in words:
        if ":" in word and ("AM" in word or "PM" in word):
            time_part = word
            break
    
    if not time_part:
        return "Invalid time format"

    if "AM" in time_part:
        time_only = time_part.replace("AM", "")
        is_pm = False
    else:
        time_only = time_part.replace("PM", "")
        is_pm = True

    hours, minutes = time_only.split(":")
    hours = int(hours)

    if is_pm and hours != 12:
        hours += 12
    elif not is_pm and hours == 12:
        hours = 0
    
    return f"{hours:02d}:{minutes}"

test_times = [
    "Train departs at 3:15PM",
    "Train arrives at 11:30AM", 
    "Departure time is 12:00AM",
    "Train leaves at 12:30PM"
]

print("TRAIN TIME PARSER")
print("-" * 25)

for time_str in test_times:
    result = convert_to_24hr(time_str)
    print(f"'{time_str}' → {result}")

print("\n" + "="*25)
user_time = input("Enter time string: ")
result = convert_to_24hr(user_time)
print(f"24-hour format: {result}")