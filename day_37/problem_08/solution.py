def calculate_cost(plan, months):
    if plan == "Basic":
        monthly_cost = 199
    elif plan == "Standard":
        monthly_cost = 499
    elif plan == "Premium":
        monthly_cost = 649
    total_cost = monthly_cost * months
    return f"₹{total_cost}"

plan = "Standard"
months = 6
result = calculate_cost(plan, months)
print(result)

result2 = calculate_cost("Basic", 12)
print(result2)

result3 = calculate_cost("Premium", 3)
print(result3)