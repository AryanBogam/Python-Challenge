def playlist_duration(durations):
    total_minutes = 0
    
    for duration in durations:
        total_minutes += duration
    
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    
    return f"{hours} hours {remaining_minutes} minutes"

durations = [5, 10, 15, 20]
result = playlist_duration(durations)
print(result)

durations2 = [30, 45, 60, 15]
result2 = playlist_duration(durations2)
print(result2)