emails = [{"subject": "Invoice", "label": "Work"}, {"subject": "Party", "label": "Personal"}]
label = "Work"

result = []
for email in emails:
    if email["label"] == label:
        result.append(email)

print(result)