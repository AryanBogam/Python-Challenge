logged_in_users = ["john", "jane", "bob", "alice"]
posts = [
    {"id": 1, "author": "john", "content": "Amazing sunset today!", "shares": 0, "shared_by": []},
    {"id": 2, "author": "jane", "content": "Python tips!", "shares": 0, "shared_by": []}
]
shared_posts = []
notifications = {}

def share_post(username, post_id, share_message=""):
    if username not in logged_in_users:
        return "Please log in first!"
    
    original_post = None
    for post in posts:
        if post["id"] == post_id:
            original_post = post
            break
    
    if not original_post:
        return "Post not found!"
    
    if username in original_post["shared_by"]:
        return "You already shared this post!"
    
    original_post["shares"] += 1
    original_post["shared_by"].append(username)
    
    shared_post = {
        "id": len(shared_posts) + 100,
        "sharer": username,
        "original_post_id": post_id,
        "share_message": share_message,
        "original_author": original_post["author"],
        "original_content": original_post["content"]
    }
    shared_posts.append(shared_post)
    
    if original_post["author"] not in notifications:
        notifications[original_post["author"]] = []
    notifications[original_post["author"]].append(f"{username} shared your post!")
    
    return "Post shared successfully!"

def get_shared_posts():
    return shared_posts

def get_post_share_count(post_id):
    for post in posts:
        if post["id"] == post_id:
            return post["shares"]
    return 0

def get_user_shared_posts(username):
    user_shares = []
    for shared in shared_posts:
        if shared["sharer"] == username:
            user_shares.append(shared)
    return user_shares

print(share_post("jane", 1, "Look at this beautiful sunset!"))
print(share_post("bob", 1, "Wow!"))
print(share_post("alice", 2))

print("Shares for post 1:", get_post_share_count(1))
print("Jane's notifications:", notifications.get("john", []))
print("Total shared posts:", len(get_shared_posts()))