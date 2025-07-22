path = []

while True:
    city = input("Enter city (or 'done'): ").strip()
    
    if city.lower() == "done":
        break
    
    path.append(city)

print("Flight path:", " → ".join(path))
