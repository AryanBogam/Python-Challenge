def calculate_fare(distance_km, class_type):
    rates = {
        "SL": 1,
        "3A": 2,
        "2A": 3,
        "1A": 4
    }
    
    if class_type not in rates:
        return "Invalid class type"
    
    fare = distance_km * rates[class_type]
    return fare

test_cases = [
    (500, "2A"),
    (300, "SL"),
    (800, "1A"),
    (200, "3A"),
    (100, "AC")
]

print("FARE CALCULATOR")
print("-" * 20)
print("Rates: SL=₹1/km, 3A=₹2/km, 2A=₹3/km, 1A=₹4/km")
print()

for distance, class_type in test_cases:
    fare = calculate_fare(distance, class_type)
    if isinstance(fare, int):
        print(f"{distance}km in {class_type}: ₹{fare}")
    else:
        print(f"{distance}km in {class_type}: {fare}")

print("\n" + "="*20)
try:
    distance = int(input("Enter distance (km): "))
    class_type = input("Enter class (SL/3A/2A/1A): ")
    result = calculate_fare(distance, class_type)
    
    if isinstance(result, int):
        print(f"Total fare: ₹{result}")
    else:
        print(f"Error: {result}")
except ValueError:
    print("Please enter valid distance")