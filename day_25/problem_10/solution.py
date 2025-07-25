import json
filename = input("Enter JSON file: ")

try:
    with open(filename, 'r') as file:
        data = json.load(file)
        print("User data:", data)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid user data")