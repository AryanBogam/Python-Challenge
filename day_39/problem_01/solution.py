def check_last_seen(contact_name, minutes_ago):
    if minutes_ago <= 5:
        return f"{contact_name} is online"
    else:
        return f"{contact_name} was last seen {minutes_ago} minutes ago"

result = check_last_seen("Aryan", 3)
print(result)

result2 = check_last_seen("Aryan", 8)
print(result2)

result3 = check_last_seen("Riya", 5)
print(result3)