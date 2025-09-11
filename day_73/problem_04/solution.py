from datetime import datetime

activity_log = {}
logged_in_users = []

def log_activity(username, action, details=""):
    if username not in activity_log:
        activity_log[username] = []
    
    log_entry = {
        "action": action,
        "time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "details": details
    }
    activity_log[username].append(log_entry)

def login_user_with_log(username):
    if username not in logged_in_users:
        logged_in_users.append(username)
    log_activity(username, "login")
    return "User logged in!"

def logout_user_with_log(username):
    if username in logged_in_users:
        logged_in_users.remove(username)
    log_activity(username, "logout")
    return "User logged out!"

def create_post_with_log(username, content):
    log_activity(username, "post_created", f"Content: {content[:20]}...")
    return "Post created!"

def comment_with_log(username, post_id, comment):
    log_activity(username, "commented", f"On post {post_id}: {comment[:20]}...")
    return "Comment added!"

def react_with_log(username, post_id, reaction):
    log_activity(username, "reacted", f"{reaction} on post {post_id}")
    return "Reaction added!"

def send_friend_request_with_log(sender, receiver):
    log_activity(sender, "friend_request_sent", f"To: {receiver}")
    return "Friend request sent!"

def get_user_activity(username, limit=10):
    if username not in activity_log:
        return "No activity found!"
    
    user_activities = activity_log[username]
    return user_activities[-limit:]

def get_activity_summary(username):
    if username not in activity_log:
        return "No activity found!"
    
    activities = activity_log[username]
    summary = {}
    
    for activity in activities:
        action = activity["action"]
        if action in summary:
            summary[action] += 1
        else:
            summary[action] = 1
    
    return summary

print(login_user_with_log("john"))
print(create_post_with_log("john", "Hello World! This is my first post."))
print(comment_with_log("john", 1, "Great post!"))
print(react_with_log("john", 1, "Like"))

print("John's recent activity:")
recent = get_user_activity("john", 5)
for activity in recent:
    print(f"{activity['time']}: {activity['action']} - {activity['details']}")

print("Activity summary:", get_activity_summary("john"))