def log_motion(events):
    for time in events:
        print(f"Motion detected at {time}")

events = ["10:30", "11:00", "12:15"]
log_motion(events)