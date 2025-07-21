vehicle_types = ["car", "bike", "car", "bus", "bike", "car"]

counts = {}
for v in vehicle_types:
    counts[v] = counts.get(v, 0) + 1

print(counts)