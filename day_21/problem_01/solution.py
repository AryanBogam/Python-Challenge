def green_light_duration(time, traffic_volume):
    time_multiplier = {
        "morning": 1.5,
        "afternoon": 1.0,
        "evening": 1.7,
        "night": 0.8
    }

    traffic_multiplier = {
        "low": 20,
        "medium": 40,
        "high": 60
    }

    base_time = traffic_multiplier.get(traffic_volume.lower(), 30)
    adjusted_time = int(base_time * time_multiplier.get(time.lower(), 1))
    return adjusted_time

print(green_light_duration("morning", "high"))