
scheduled = input("Enter scheduled arrival time (HH:MM): ")
actual = input("Enter actual arrival time (HH:MM): ")

scheduled_hour, scheduled_minute = scheduled.split(":")
actual_hour, actual_minute = actual.split(":")

scheduled_hour = int(scheduled_hour)
scheduled_minute = int(scheduled_minute)
actual_hour = int(actual_hour)
actual_minute = int(actual_minute)

scheduled_total = scheduled_hour * 60 + scheduled_minute
actual_total = actual_hour * 60 + actual_minute

delay = actual_total - scheduled_total

print("Flight delay:", delay, "minutes")
