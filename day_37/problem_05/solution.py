def format_duration(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

seconds = 3670
result = format_duration(seconds)
print(result)

seconds2 = 7825
result2 = format_duration(seconds2)
print(result2)