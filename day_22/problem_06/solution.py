current_altitude = int(input("Enter current altitude (in feet): "))
required_altitude = int(input("Enter required minimum altitude (in feet): "))

if current_altitude >= required_altitude:
    print("Clear for flight.")
else:
    print("Increase altitude!")
