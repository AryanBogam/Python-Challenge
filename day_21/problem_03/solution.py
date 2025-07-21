from collections import defaultdict

def track_violations(violations):
    vehicle_counts = defaultdict(int)
    flagged = {}

    for v in violations:
        if v["light"].lower() == "red":
            vehicle_counts[v["vehicle"]] += 1

    for vehicle, count in vehicle_counts.items():
        flagged[vehicle] = {
            "violations": count,
            "flagged": count > 3
        }

    return flagged

violations = [
    {"vehicle": "MH12AB1234", "time": "10:05", "light": "red"},
    {"vehicle": "MH12AB1234", "time": "10:10", "light": "red"},
    {"vehicle": "MH12AB1234", "time": "10:15", "light": "red"},
    {"vehicle": "MH12AB1234", "time": "10:20", "light": "red"},
    {"vehicle": "MH12XY9999", "time": "10:30", "light": "red"},
]
print(track_violations(violations))
