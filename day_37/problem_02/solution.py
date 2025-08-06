def check_plan(plan):
    if plan == "Basic":
        return "480p quality, 1 screen"
    elif plan == "Standard":
        return "1080p quality, 2 screens"
    elif plan == "Premium":
        return "4K quality, 4 screens"

plan = "Premium"
result = check_plan(plan)
print(result)
result2 = check_plan("Basic")
print(result2)
result3 = check_plan("Standard")
print(result3)