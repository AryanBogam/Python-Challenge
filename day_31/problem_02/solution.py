workers = ["Alice", "Bob", "Charlie"]
shifts = ["Morning", "Evening", "Night"]

day = int(input("Enter day (0=Monday, 1=Tuesday, etc.): "))

print(f"Shift Schedule for Day {day}:")
print("-" * 30)

for i, worker in enumerate(workers):
    shift_index = (day + i) % len(shifts)
    assigned_shift = shifts[shift_index]
    print(f"{worker}: {assigned_shift}")

print("-" * 30)
print("Note: Shifts rotate daily to prevent same assignments")