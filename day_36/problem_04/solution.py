def format_duration(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02d}:{remaining_seconds:02d}"

seconds = 125
result = format_duration(seconds)
print(result)

seconds2 = 65
result2 = format_duration(seconds2)
print(result2)