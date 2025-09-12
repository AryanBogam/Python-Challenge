subscriptions = {}

def subscribe(username, creator):
    if username not in subscriptions:
        subscriptions[username] = []
    if creator not in subscriptions[username]:
        subscriptions[username].append(creator)
        return f"{username} subscribed to {creator}"
    return f"{username} is already subscribed to {creator}"

def unsubscribe(username, creator):
    if username in subscriptions and creator in subscriptions[username]:
        subscriptions[username].remove(creator)
        return f"{username} unsubscribed from {creator}"
    return f"{username} is not subscribed to {creator}"

subscribe("user1", "Aryan")
subscribe("user1", "Chef")
print(subscriptions)
unsubscribe("user1", "Chef")
print(subscriptions)