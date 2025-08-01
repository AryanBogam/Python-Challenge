def format_bio(name, age, location):
    bio = f"{name} | {age} | {location} 🌍 #PythonDev"
    return bio

name = input("Enter your name: ")
age = input("Enter your age: ")
location = input("Enter your location: ")

formatted_bio = format_bio(name, age, location)
print(f"\nYour Twitter bio:")
print(formatted_bio)