flights = [["AI101", 25], ["BA209", 45], ["QF302", 28]]

emergency_flights = []

for flight in flights:
    flight_id, fuel = flight
    if fuel < 30:
        emergency_flights.append(flight_id)

if emergency_flights:
    print("Flights in fuel emergency:", ", ".join(emergency_flights))
else:
    print("All flights have safe fuel levels.")
