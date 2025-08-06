def watch_progress(watched, total):
    percentage = (watched / total) * 100
    return f"{percentage}%"

watched = 45
total = 60
result = watch_progress(watched, total)
print(result)

watched2 = 20
total2 = 80
result2 = watch_progress(watched2, total2)
print(result2)