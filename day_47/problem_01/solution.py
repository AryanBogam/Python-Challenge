emails = [{"subject": "Hi", "read": False}, {"subject": "Work", "read": True}]

count = 0
for email in emails:
    if email["read"] == False:
        count = count + 1

print(count)