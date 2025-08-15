def calculate_total_earnings(bookings):
    total = sum(bookings)
    return total

bookings = [200, 300, 150]
result = calculate_total_earnings(bookings)
print(result)

print(calculate_total_earnings([100, 250, 180, 320]))
print(calculate_total_earnings([500]))
print(calculate_total_earnings([75, 90, 125, 200, 300]))
print(calculate_total_earnings([]))