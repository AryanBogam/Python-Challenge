def calculate_eta(distance_km, speed_kmh):
    if speed_kmh <= 0:
        return "Invalid speed"
    
    time_hours = distance_km / speed_kmh
    time_minutes = time_hours * 60
    
    # Rounding to nearest minute
    eta_minutes = round(time_minutes)
    
    return eta_minutes

result = calculate_eta(50, 60)
print(f"{result} minutes")