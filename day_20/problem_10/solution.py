def is_spam(message, history):
    links = message.lower().count("http")
    caps = sum(1 for word in message.split() if word.isupper())
    repeated = history.count(message)

    if links > 2 or caps > 5 or repeated > 1:
        return "Spam"
    return "Safe"
history = [
    "BUY NOW http://scam.com", 
    "BUY NOW http://scam.com", 
    "BUY NOW http://scam.com"
]
msg = "BUY NOW http://scam.com"

print(is_spam(msg, history))
