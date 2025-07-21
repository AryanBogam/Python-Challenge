def detect_peak_hours(traffic_log):
    max_vehicles = max(entry["vehicles"] for entry in traffic_log)
    peak_hours = [entry["hour"] for entry in traffic_log if entry["vehicles"] == max_vehicles]
    return peak_hours

traffic_log = [
    {"hour": "08:00", "vehicles": 120},
    {"hour": "09:00", "vehicles": 250},
    {"hour": "10:00", "vehicles": 250}
]
print(detect_peak_hours(traffic_log))
