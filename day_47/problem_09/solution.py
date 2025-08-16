emails = [{"subject": "Boss", "important": True}, {"subject": "Spam", "important": False}]

result = []
for email in emails:
    if email["important"] == True:
        result.append(email)

print(result)