favorite_places = {}

print("Enter favorite places (type 'done' when finished):")

while True:
    name = input("Enter person's name: ")
    if name == "done":
        break
    
    place = input("Enter their favorite place: ")
    favorite_places[name] = place

print("\nEveryone's favorite places:")
for name, place in favorite_places.items():
    print(name + "'s favorite place is " + place)