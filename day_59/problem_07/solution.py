guests = []

print("Welcome to the Guest Book!")
print("Enter guest names (type 'stop' to finish):")

while True:
    name = input("Enter guest name: ")
    if name == "stop":
        break
    guests.append(name)
    print("Guest added!")

print("\nGuest List:")
for guest in guests:
    print("-", guest)

print("Total guests:", len(guests))