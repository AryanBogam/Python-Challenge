def search_messages(messages, keyword):
    found_messages = []
    for message in messages:
        if keyword in message.lower():
            found_messages.append(message)
    count = len(found_messages)
    return f"Found {count} messages containing '{keyword}'"

messages = [
    "Let's have a meeting tomorrow",
    "The meeting was great",
    "I'll send the files later",
    "Meeting room is booked",
    "Good morning everyone"
]

result = search_messages(messages, "meeting")
print(result)

result2 = search_messages(messages, "files")
print(result2)