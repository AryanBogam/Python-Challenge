emails = [{"subject": "Project", "starred": True}, {"subject": "Hello", "starred": False}]

count = 0
for email in emails:
    if email["starred"] == True:
        count = count + 1

print(count)