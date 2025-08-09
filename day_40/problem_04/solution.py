def filter_hype_messages(messages):
    hype_messages = []
    for message in messages:
        if "hype" in message.lower():
            hype_messages.append(message)
    return hype_messages

messages = ["let's go", "hype!", "nice stream"]
result = filter_hype_messages(messages)
print(result)

messages2 = ["HYPE TRAIN!", "good game", "so much hype", "amazing"]
result2 = filter_hype_messages(messages2)
print(result2)