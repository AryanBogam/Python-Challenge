from datetime import datetime

logged_in_users = ["john", "jane"]
posts = [
    {"id": 1, "author": "john", "content": "Hello World!", "created_at": "2023-01-01", "updated_at": None},
    {"id": 2, "author": "jane", "content": "Great day!", "created_at": "2023-01-01", "updated_at": None}
]
next_post_id = 3

def create_post(username, content):
    global next_post_id
    if username not in logged_in_users:
        return "Please log in first!"
    
    post = {
        "id": next_post_id,
        "author": username,
        "content": content,
        "created_at": str(datetime.now().date()),
        "updated_at": None
    }
    posts.append(post)
    next_post_id += 1
    return "Post created successfully!"

def edit_post(username, post_id, new_content):
    if username not in logged_in_users:
        return "Please log in first!"
    
    for post in posts:
        if post["id"] == post_id:
            if post["author"] != username:
                return "You can only edit your own posts!"
            
            post["content"] = new_content
            post["updated_at"] = str(datetime.now().date())
            return "Post edited successfully!"
    
    return "Post not found!"

def delete_post(username, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    for i, post in enumerate(posts):
        if post["id"] == post_id:
            if post["author"] != username:
                return "You can only delete your own posts!"
            
            posts.pop(i)
            return "Post deleted successfully!"
    
    return "Post not found!"

print(edit_post("john", 1, "Updated content!"))
print(delete_post("jane", 2))
print(posts)