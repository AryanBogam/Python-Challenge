def parse_reminder(text):
    parts = text.lower().split(" ")
    date = parts[2]
    time = parts[4] + ":00"
    task = " ".join(parts[6:])
    return {"task": task, "time": time, "date": date}

print(parse_reminder("remind me tomorrow at 8 to walk dog"))
