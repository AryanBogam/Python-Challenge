def calculate_vm_cost(vm_size, hours):
    """
    Calculates VM cost based on size and hours used
    """
    rates = {
        "B1": 0.02,
        "B2": 0.05,
        "B4": 0.10
    }

    if vm_size in rates:
        hourly_rate = rates[vm_size]
        total_cost = hourly_rate * hours
        return total_cost
    else:
        return "Invalid VM size"

vm_size = "B2"
hours = 10
cost = calculate_vm_cost(vm_size, hours)
print(f"VM {vm_size} for {hours} hours: ${cost}")

test_cases = [
    ("B1", 5),
    ("B2", 10), 
    ("B4", 3),
    ("B8", 2)
]

for size, hrs in test_cases:
    result = calculate_vm_cost(size, hrs)
    print(f"{size} for {hrs} hours: ${result}")