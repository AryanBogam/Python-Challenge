def average_watch_time(watch_times):
    total = 0
    
    for time in watch_times:
        total += time
    
    average = total / len(watch_times)
    return f"{average} minutes"

watch_times = [5, 8, 10, 7]
result = average_watch_time(watch_times)
print(result)

watch_times2 = [3, 6, 9]
result2 = average_watch_time(watch_times2)
print(result2)