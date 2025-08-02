def is_direct_route(start, end, route):
    if start not in route or end not in route:
        return False

    start_index = route.index(start)
    end_index = route.index(end)

    return start_index < end_index

route = ["Mumbai", "Pune", "Solapur", "Hyderabad", "Chennai"]

test_cases = [
    ("Mumbai", "Chennai"),
    ("Hyderabad", "Pune"),
    ("Mumbai", "Pune"),
    ("Delhi", "Mumbai")
]

print("TRAIN ROUTE FINDER")
print("-" * 25)
print(f"Route: {' → '.join(route)}")
print()

for start, end in test_cases:
    result = is_direct_route(start, end, route)
    print(f"{start} to {end}: {result}")

print("\n" + "="*25)
start_station = input("Enter start station: ")
end_station = input("Enter end station: ")
result = is_direct_route(start_station, end_station, route)
print(f"Direct route available: {result}")