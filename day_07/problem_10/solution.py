battery = 100
hours = 0

while battery >= 10:
    print(f"Hour {hours}: Battery at {battery}%")
    battery -= 7
    hours += 1

print(f"Battery dropped below 10% after {hours} hours.")
