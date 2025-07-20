def health_alert(heart_rates, motions):
    alerts = []
    for i in range(len(heart_rates)):
        if heart_rates[i] > 180:
            alerts.append(f"High heart rate at minute {i}")
        if motions[i] < 1 and heart_rates[i] > 120:
            alerts.append(f"Possible fall detected at minute {i}")
    return alerts

print(health_alert([85, 122, 190, 130], [3, 2, 0, 0]))
