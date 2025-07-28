cities = {"Mumbai": 12000000, "Delhi": 11000000, "Bangalore": 8000000}

city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

try:
    pop1 = cities[city1]
    pop2 = cities[city2]
    difference = abs(pop1 - pop2)
    print(f"Population difference: {difference}")
except KeyError:
    if city1 not in cities and city2 not in cities:
        print("Both cities not found")
    elif city1 not in cities:
        print(f"{city1} not found")
    else:
        print(f"{city2} not found")