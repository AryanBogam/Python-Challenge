users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"}
}
logged_in_users = ["john", "jane"]
posts = []

def create_post(username, content):
    if username not in logged_in_users:
        return "Please log in first!"
    
    post = {
        "author": username,
        "content": content,
        "likes": 0
    }
    posts.append(post)
    return "Post created successfully!"

def view_newsfeed():
    if not posts:
        return "No posts to show!"
    
    feed = []
    for post in posts:
        feed.append(f"{post['author']}: {post['content']} (Likes: {post['likes']})")
    
    return feed

print(create_post("john", "Hello World!"))
print(create_post("jane", "Having a great day!"))
print(create_post("bob", "Not logged in"))

newsfeed = view_newsfeed()
for post in newsfeed:
    print(post)