def toggle_night_vision(current_state):
    if current_state == "OFF":
        return "Night vision turned ON"
    else:
        return "Night vision turned OFF"

result = toggle_night_vision("OFF")
print(result)

result2 = toggle_night_vision("ON")
print(result2)