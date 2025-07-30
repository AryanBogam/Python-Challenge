temps = [35.5, 38.2, 33.0, 36.6, 37.8, 32.1]

fever_temps = []
for temp in temps:
    if temp > 37.5:
        fever_temps.append(temp)

print(f"All temperatures: {temps}")
print(f"Fever temperatures (>37.5): {fever_temps}")