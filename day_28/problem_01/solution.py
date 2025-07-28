contacts = {"Alice": "9123456789", "Bob": "9000000000"}

name = input("Enter name: ")

try:
    phone = contacts[name]
    print(f"{name}: {phone}")
except KeyError:
    print("Contact not found.")