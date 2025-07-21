def check_speed(speed):
    if speed > 60:
        return "Fine ₹1000"
    else:
        return "No Fine"

print(check_speed(70))