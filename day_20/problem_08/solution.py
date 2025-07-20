def prioritize_appointments(customers):
    def priority(customer):
        is_urgent = customer['device'] == "iPhone" and "battery" in customer['issue'].lower()
        return (not is_urgent, customer['time'])

    sorted_customers = sorted(customers, key=priority)
    return sorted_customers

appointments = [
    {"name": "Alice", "time": "12:00", "device": "MacBook", "issue": "Screen"},
    {"name": "Bob", "time": "11:00", "device": "iPhone", "issue": "Battery draining fast"},
    {"name": "Charlie", "time": "10:00", "device": "iPhone", "issue": "Speaker issue"}
]

print(prioritize_appointments(appointments))
