emails = [
    {"subject": "Meeting", "body": "Project discussion"},
    {"subject": "Party", "body": "Birthday celebration"}
]
keyword = "Project"

result = []
for email in emails:
    if keyword in email["subject"] or keyword in email["body"]:
        result.append(email)

print(result)