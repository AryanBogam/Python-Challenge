emails = [
    {"subject": "Hello", "thread_id": 1},
    {"subject": "Reply", "thread_id": 1},
    {"subject": "New Topic", "thread_id": 2}
]

result = {}
for email in emails:
    thread_id = email["thread_id"]
    if thread_id not in result:
        result[thread_id] = []
    result[thread_id].append(email["subject"])

print(result)