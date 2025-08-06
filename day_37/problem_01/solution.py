def total_watch_time(times):
    total_minutes = 0
    for time in times:
        total_minutes += time
    
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    
    return f"{hours} hours {remaining_minutes} minutes"

times = [45, 30, 60, 50]
result = total_watch_time(times)
print(result)

times2 = [90, 120, 30]
result2 = total_watch_time(times2)
print(result2)