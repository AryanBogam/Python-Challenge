def check_cost_alert(current_bill, threshold):
    if current_bill > threshold:
        return "Cost alert triggered!"
    else:
        return "No alert"

current_bill = 80
threshold = 100
result = check_cost_alert(current_bill, threshold)
print(f"Current bill: ${current_bill}, Threshold: ${threshold}")
print(f"Result: {result}")

print("\n" + "="*30)
 
test_cases = [
    (80, 100),
    (120, 100),
    (100, 100),
    (150, 200)
]

for bill, limit in test_cases:
    result = check_cost_alert(bill, limit)
    print(f"Bill: ${bill}, Limit: ${limit} -> {result}")

def cost_alert_details(current_bill, threshold):
    if current_bill > threshold:
        over_by = current_bill - threshold
        return f"Cost alert triggered! Over budget by ${over_by}"
    else:
        remaining = threshold - current_bill
        return f"No alert. ${remaining} remaining in budget"

print("\nDetailed cost analysis:")
for bill, limit in test_cases:
    details = cost_alert_details(bill, limit)
    print(f"${bill}/${limit}: {details}")