def detect_accident(speeds):
    for i in range(len(speeds) - 2):
        if speeds[i] > 30 and speeds[i+1] == 0 and speeds[i+2] == 0:
            return "Possible accident detected!"
    return "No accident detected."

speeds = [45, 40, 20, 0, 0, 0, 35]
print(detect_accident(speeds))
