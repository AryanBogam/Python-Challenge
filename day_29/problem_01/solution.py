temps = (31.2, 30.8, 32.1, 35.6, 34.2, 33.5)

highest = max(temps)
lowest = min(temps)
average = sum(temps) / len(temps)

print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average:.1f}")