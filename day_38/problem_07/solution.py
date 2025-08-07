def can_send_request(existing_friends, username):
    if username in existing_friends:
        return "Already Friends"
    else:
        return "Request Sent"

result = can_send_request(["arya", "rahul"], "mira")
print(result)

result2 = can_send_request(["arya", "rahul"], "arya")
print(result2)

result3 = can_send_request(["john", "jane"], "bob")
print(result3)