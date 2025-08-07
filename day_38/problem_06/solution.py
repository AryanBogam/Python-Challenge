def snapcode_status(minutes_left):
    if minutes_left > 0:
        return "Unlocked"
    else:
        return "Locked"

result = snapcode_status(10)
print(result)

result2 = snapcode_status(0)
print(result2)

result3 = snapcode_status(-5)
print(result3)