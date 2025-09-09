logged_in_users = ["john", "jane", "bob"]
friends = {"john": ["jane"], "jane": ["john"], "bob": []}
posts = [
    {"id": 1, "author": "john", "content": "Public post", "privacy": "public"},
    {"id": 2, "author": "jane", "content": "Friends only", "privacy": "friends"},
    {"id": 3, "author": "bob", "content": "Private post", "privacy": "private"}
]

def create_post_with_privacy(username, content, privacy="public"):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if privacy not in ["public", "friends", "private"]:
        return "Invalid privacy setting! Use: public, friends, or private"
    
    post = {
        "id": len(posts) + 1,
        "author": username,
        "content": content,
        "privacy": privacy
    }
    posts.append(post)
    return "Post created successfully!"

def view_newsfeed(viewer):
    if viewer not in logged_in_users:
        return "Please log in first!"
    
    visible_posts = []
    
    for post in posts:
        if post["privacy"] == "public":
            visible_posts.append(post)
        elif post["privacy"] == "friends":
            if viewer == post["author"] or viewer in friends.get(post["author"], []):
                visible_posts.append(post)
        elif post["privacy"] == "private":
            if viewer == post["author"]:
                visible_posts.append(post)
    
    return visible_posts

print(create_post_with_privacy("john", "New public post", "public"))
print(create_post_with_privacy("jane", "Friends only post", "friends"))

john_feed = view_newsfeed("john")
bob_feed = view_newsfeed("bob")

print("John sees:", len(john_feed), "posts")
print("Bob sees:", len(bob_feed), "posts")