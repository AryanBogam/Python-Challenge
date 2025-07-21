def calculate_total_fine(violations):
    rates = {
        "signal_jump": 1000,
        "speeding": 500
    }
    total = 0
    for v in violations:
        total += rates.get(v["type"], 0) * v["count"]
    return total

violations = [
    {"type": "signal_jump", "count": 2},
    {"type": "speeding", "count": 3}
]
print("Total Fine: ₹", calculate_total_fine(violations))