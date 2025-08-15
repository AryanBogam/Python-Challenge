def calculate_total_cost(nightly_rate, nights):
    total = nightly_rate * nights
    return total

nightly_rate = 100
nights = 3
result = calculate_total_cost(nightly_rate, nights)
print(result)

print(calculate_total_cost(150, 2))
print(calculate_total_cost(80, 5))
print(calculate_total_cost(200, 1))