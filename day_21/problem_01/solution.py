def get_light_color(time):
    if 0 <= time <= 30:
        return "Green"
    elif 31 <= time <= 40:
        return "Yellow"
    elif 41 <= time <= 60:
        return "Red"
    else:
        return "Invalid time"

print(get_light_color(25))