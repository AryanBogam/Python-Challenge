emails = [
    {"subject": "Report", "attachments": ["report.pdf"]},
    {"subject": "Hi", "attachments": []}
]

result = []
for email in emails:
    if len(email["attachments"]) > 0:
        result.append(email)

print(result)