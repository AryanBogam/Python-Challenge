users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"}
}
logged_in_users = ["john", "jane"]
messages = {}

def send_message(sender, receiver, message):
    if sender not in logged_in_users:
        return "Please log in first!"
    
    if receiver not in users:
        return "User not found!"
    
    if sender not in messages:
        messages[sender] = {}
    if receiver not in messages[sender]:
        messages[sender][receiver] = []
    
    messages[sender][receiver].append(message)
    return "Message sent!"

def read_messages(username, from_user):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if from_user not in messages or username not in messages[from_user]:
        return "No messages from this user!"
    
    return messages[from_user][username]

print(send_message("john", "jane", "Hi Jane!"))
print(send_message("jane", "john", "Hello John!"))
print(send_message("john", "jane", "How are you?"))

print(read_messages("jane", "john"))
print(read_messages("john", "jane"))