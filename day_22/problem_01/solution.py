runway_free = True

response = input("Plane requests landing. Is runway free? (yes/no): ").strip().lower()

if response == "yes":
    if runway_free:
        print("Landing granted")
        runway_free = False
    else:
        print("Permission denied")
else:
    print("Permission denied")
