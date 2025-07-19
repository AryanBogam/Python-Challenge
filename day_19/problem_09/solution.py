distances = [12.5, 20.1, 5.0, 15.2, 10.3]

def delivery_stats(dist_list):
    total = sum(dist_list)
    avg = total / len(dist_list)
    return total, avg

total_km, avg_km = delivery_stats(distances)
print(f"Total: {total_km} km, Average: {avg_km:.2f} km")