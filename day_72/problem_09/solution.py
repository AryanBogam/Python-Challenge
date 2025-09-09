users = {
    "john": {"email": "john@email.com", "saved_posts": []},
    "jane": {"email": "jane@email.com", "saved_posts": []},
    "bob": {"email": "bob@email.com", "saved_posts": []}
}
logged_in_users = ["john", "jane", "bob"]
posts = [
    {"id": 1, "author": "jane", "content": "Beautiful sunset today!"},
    {"id": 2, "author": "bob", "content": "Python tips and tricks"},
    {"id": 3, "author": "john", "content": "Great food at new restaurant"}
]

def save_post(username, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    post_found = False
    for post in posts:
        if post["id"] == post_id:
            post_found = True
            break
    
    if not post_found:
        return "Post not found!"
    
    if post_id in users[username]["saved_posts"]:
        return "Post already saved!"
    
    users[username]["saved_posts"].append(post_id)
    return "Post saved successfully!"

def unsave_post(username, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if post_id in users[username]["saved_posts"]:
        users[username]["saved_posts"].remove(post_id)
        return "Post removed from saved!"
    
    return "Post not in saved list!"

def get_saved_posts(username):
    if username not in logged_in_users:
        return "Please log in first!"
    
    saved_post_ids = users[username]["saved_posts"]
    saved_posts = []
    
    for post in posts:
        if post["id"] in saved_post_ids:
            saved_posts.append(post)
    
    return saved_posts

def is_post_saved(username, post_id):
    if username not in logged_in_users:
        return False
    
    return post_id in users[username]["saved_posts"]

print(save_post("john", 1))
print(save_post("john", 2))
print(save_post("jane", 1))

print("John's saved posts:", len(get_saved_posts("john")))
print("Is post 1 saved by john?", is_post_saved("john", 1))

print(unsave_post("john", 1))
print("John's saved posts after unsaving:", len(get_saved_posts("john")))