def check_milestone(subscribers):
    if subscribers >= 1000000:
        return "Gold Play Button"
    elif subscribers >= 100000:
        return "Silver Play Button"
    else:
        return "Keep going!"

subscribers = 250000
result = check_milestone(subscribers)
print(result)

result2 = check_milestone(1500000)
print(result2)

result3 = check_milestone(50000)
print(result3)