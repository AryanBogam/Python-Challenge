users = {
    "john": {"email": "john@email.com"},
    "jane": {"email": "jane@email.com"},
    "bob": {"email": "bob@email.com"},
    "raj": {"email": "raj@email.com"}
}
logged_in_users = ["john", "jane", "bob"]
posts = []
notifications = {}

def create_post_with_tags(author, content):
    if author not in logged_in_users:
        return "Please log in first!"
    
    tags = []
    words = content.split()
    
    for word in words:
        if word.startswith("@"):
            username = word[1:]
            if username in users:
                tags.append(username)
    
    post = {
        "id": len(posts) + 1,
        "author": author,
        "content": content,
        "tags": tags
    }
    posts.append(post)
    
    for tagged_user in tags:
        if tagged_user not in notifications:
            notifications[tagged_user] = []
        notifications[tagged_user].append(f"{author} tagged you in a post: {content}")
    
    return "Post created successfully!"

def get_posts_with_user_tagged(username):
    tagged_posts = []
    
    for post in posts:
        if username in post["tags"]:
            tagged_posts.append(post)
    
    return tagged_posts

def view_notifications(username):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if username not in notifications:
        return "No notifications!"
    
    return notifications[username]

print(create_post_with_tags("john", "Had lunch with @jane and @bob today!"))
print(create_post_with_tags("jane", "Thanks @john for the great time!"))

print("Bob's notifications:", view_notifications("bob"))
print("Posts where jane is tagged:", len(get_posts_with_user_tagged("jane")))