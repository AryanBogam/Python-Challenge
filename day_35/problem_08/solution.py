def auto_shutdown(current_hour):
    if current_hour >= 1 and current_hour <= 5:
        return "Auto shutdown activated"
    else:
        return "Camera active"

result = auto_shutdown(2)
print(result)

result2 = auto_shutdown(10)
print(result2)

result3 = auto_shutdown(5)
print(result3)