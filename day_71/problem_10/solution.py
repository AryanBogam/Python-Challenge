users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"}
}
logged_in_users = ["john", "jane"]
notifications = {}

def add_notification(username, message):
    if username not in notifications:
        notifications[username] = []
    notifications[username].append(message)

def send_friend_request_with_notification(sender, receiver):
    if sender not in logged_in_users:
        return "Please log in first!"
    
    if receiver not in users:
        return "User not found!"
    
    add_notification(receiver, f"{sender} sent you a friend request!")
    return "Friend request sent!"

def like_post_with_notification(liker, post_author):
    if liker not in logged_in_users:
        return "Please log in first!"
    
    add_notification(post_author, f"{liker} liked your post!")
    return "Post liked!"

def comment_with_notification(commenter, post_author, comment):
    if commenter not in logged_in_users:
        return "Please log in first!"
    
    add_notification(post_author, f"{commenter} commented on your post: {comment}")
    return "Comment added!"

def view_notifications(username):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if username not in notifications:
        return "No notifications!"
    
    return notifications[username]

print(send_friend_request_with_notification("john", "jane"))
print(like_post_with_notification("jane", "john"))
print(comment_with_notification("jane", "john", "Great post!"))

print(view_notifications("john"))
print(view_notifications("jane"))