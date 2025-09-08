logged_in_users = ["john", "jane"]
posts = [
    {"author": "john", "content": "Hello World!", "likes": 0, "liked_by": [], "comments": []},
    {"author": "jane", "content": "Having a great day!", "likes": 0, "liked_by": [], "comments": []}
]

def like_post(username, post_index):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if post_index < 0 or post_index >= len(posts):
        return "Post not found!"
    
    post = posts[post_index]
    
    if username in post["liked_by"]:
        post["liked_by"].remove(username)
        post["likes"] -= 1
        return "Post unliked!"
    else:
        post["liked_by"].append(username)
        post["likes"] += 1
        return "Post liked!"

def comment_on_post(username, post_index, comment):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if post_index < 0 or post_index >= len(posts):
        return "Post not found!"
    
    posts[post_index]["comments"].append(f"{username}: {comment}")
    return "Comment added!"

print(like_post("jane", 0))
print(like_post("john", 0))
print(comment_on_post("jane", 0, "Great post!"))
print(posts[0])