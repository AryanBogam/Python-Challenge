logged_in_users = ["john", "jane", "bob"]
posts = [
    {"id": 1, "author": "john", "content": "Welcome to my profile!"},
    {"id": 2, "author": "john", "content": "Another post"},
    {"id": 3, "author": "jane", "content": "Jane's post"}
]
user_profiles = {
    "john": {"pinned_post": None},
    "jane": {"pinned_post": None},
    "bob": {"pinned_post": None}
}
groups = {
    "python_lovers": {"admin": "john", "members": ["john", "jane"], "pinned_post": None}
}

def pin_post_to_profile(username, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    post_found = False
    for post in posts:
        if post["id"] == post_id and post["author"] == username:
            post_found = True
            break
    
    if not post_found:
        return "Can only pin your own posts!"
    
    user_profiles[username]["pinned_post"] = post_id
    return "Post pinned to profile!"

def unpin_post_from_profile(username):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if user_profiles[username]["pinned_post"] is None:
        return "No post is pinned!"
    
    user_profiles[username]["pinned_post"] = None
    return "Post unpinned from profile!"

def pin_post_to_group(username, group_name, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if group_name not in groups:
        return "Group not found!"
    
    if groups[group_name]["admin"] != username:
        return "Only group admin can pin posts!"
    
    post_found = False
    for post in posts:
        if post["id"] == post_id:
            post_found = True
            break
    
    if not post_found:
        return "Post not found!"
    
    groups[group_name]["pinned_post"] = post_id
    return "Post pinned to group!"

def get_profile_posts(username):
    user_posts = []
    pinned_id = user_profiles[username]["pinned_post"]
    
    for post in posts:
        if post["author"] == username:
            if post["id"] == pinned_id:
                pinned_post = post.copy()
                pinned_post["pinned"] = True
                user_posts.insert(0, pinned_post)
            else:
                user_posts.append(post)
    
    return user_posts

def get_group_posts(group_name):
    if group_name not in groups:
        return "Group not found!"
    
    group_posts = []
    pinned_id = groups[group_name]["pinned_post"]
    
    if pinned_id:
        for post in posts:
            if post["id"] == pinned_id:
                pinned_post = post.copy()
                pinned_post["pinned"] = True
                group_posts.append(pinned_post)
                break
    
    return group_posts

print(pin_post_to_profile("john", 1))
print(pin_post_to_group("john", "python_lovers", 2))

profile_posts = get_profile_posts("john")
print("John's profile posts:")
for post in profile_posts:
    pinned_text = " (PINNED)" if post.get("pinned") else ""
    print(f"- {post['content']}{pinned_text}")

print(unpin_post_from_profile("john"))
print("Pinned post after unpinning:", user_profiles["john"]["pinned_post"])