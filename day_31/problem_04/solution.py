meetings = [("09:00", "10:30"), ("10:00", "11:00"), ("11:30", "12:30")]

def check_conflict(meetings):
    def time_to_minutes(time_str):
        hours, minutes = time_str.split(":")
        return int(hours) * 60 + int(minutes)
    
    for i in range(len(meetings)):
        for j in range(i + 1, len(meetings)):
            start1, end1 = meetings[i]
            start2, end2 = meetings[j]

            start1_min = time_to_minutes(start1)
            end1_min = time_to_minutes(end1)
            start2_min = time_to_minutes(start2)
            end2_min = time_to_minutes(end2)
            
            if start1_min < end2_min and start2_min < end1_min:
                return True
    
    return False

has_conflict = check_conflict(meetings)
print("Meeting Schedule:")
for i, (start, end) in enumerate(meetings, 1):
    print(f"Meeting {i}: {start} - {end}")

print(f"\nConflict detected: {has_conflict}")