users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"},
    "bob": {"email": "bob@email.com", "password": "pass789"}
}
logged_in_users = ["john", "jane"]
friend_requests = {}
friends = {}

def send_friend_request(sender, receiver):
    if sender not in logged_in_users:
        return "Please log in first!"
    
    if receiver not in users:
        return "User not found!"
    
    if sender == receiver:
        return "Cannot send request to yourself!"
    
    if receiver not in friend_requests:
        friend_requests[receiver] = []
    
    if sender in friend_requests[receiver]:
        return "Friend request already sent!"
    
    friend_requests[receiver].append(sender)
    return "Friend request sent!"

def accept_friend_request(user, sender):
    if user not in logged_in_users:
        return "Please log in first!"
    
    if user not in friend_requests or sender not in friend_requests[user]:
        return "No friend request from this user!"
    
    if user not in friends:
        friends[user] = []
    if sender not in friends:
        friends[sender] = []
    
    friends[user].append(sender)
    friends[sender].append(user)
    friend_requests[user].remove(sender)
    return "Friend request accepted!"

print(send_friend_request("john", "jane"))
print(send_friend_request("john", "bob"))
print(accept_friend_request("jane", "john"))
print(friends)