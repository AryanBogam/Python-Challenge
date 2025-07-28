data = {"A": 20, "B": 0, "C": 5}

key = input("Enter key (A, B, or C): ")

try:
    value = data[key]
    result = 100 / value
    print(f"100 / {value} = {result}")
except KeyError:
    print("Key not found")
except ZeroDivisionError:
    print("Cannot divide by zero")