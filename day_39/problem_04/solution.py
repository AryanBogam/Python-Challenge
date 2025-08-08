def check_status_expiry(hours_ago):
    if hours_ago > 24:
        return "Status expired"
    else:
        return "Status is active"

result = check_status_expiry(10)
print(result)

result2 = check_status_expiry(25)
print(result2)

result3 = check_status_expiry(24)
print(result3)