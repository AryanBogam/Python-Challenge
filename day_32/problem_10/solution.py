def parse_schedule(schedule_string):
    times_part = schedule_string.replace("Tweet at ", "")

    time_strings = times_part.split(", ")

    schedule_24hr = []
    
    for time_str in time_strings:
        time_str = time_str.strip()
        
        if "AM" in time_str:
            hour = int(time_str.replace("AM", ""))
            if hour == 12:
                hour = 0 
            schedule_24hr.append(f"{hour:02d}:00")
            
        elif "PM" in time_str: 
            hour = int(time_str.replace("PM", ""))
            if hour != 12:
                hour += 12
            schedule_24hr.append(f"{hour:02d}:00")
    
    return schedule_24hr

test_schedules = [
    "Tweet at 9AM, 3PM",
    "Tweet at 12AM, 12PM",
    "Tweet at 6AM, 8PM"
]

print("TWEET SCHEDULER PARSER")
print("-" * 30)

for schedule in test_schedules:
    parsed = parse_schedule(schedule)
    print(f"Input: '{schedule}'")
    print(f"Output: {parsed}")
    print()