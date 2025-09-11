logged_in_users = ["john", "jane", "bob"]
posts = [
    {"id": 1, "author": "john", "content": "Great day!", "reactions": {"Like": 0, "Love": 0, "Haha": 0, "Wow": 0, "Sad": 0, "Angry": 0}, "user_reactions": {}}
]

def react_to_post(username, post_id, reaction):
    if username not in logged_in_users:
        return "Please log in first!"
    
    valid_reactions = ["Like", "Love", "Haha", "Wow", "Sad", "Angry"]
    if reaction not in valid_reactions:
        return "Invalid reaction!"
    
    for post in posts:
        if post["id"] == post_id:
            if username in post["user_reactions"]:
                old_reaction = post["user_reactions"][username]
                post["reactions"][old_reaction] -= 1
            
            post["user_reactions"][username] = reaction
            post["reactions"][reaction] += 1
            return f"Reacted with {reaction}!"
    
    return "Post not found!"

def remove_reaction(username, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    for post in posts:
        if post["id"] == post_id:
            if username in post["user_reactions"]:
                old_reaction = post["user_reactions"][username]
                post["reactions"][old_reaction] -= 1
                del post["user_reactions"][username]
                return "Reaction removed!"
            return "No reaction to remove!"
    
    return "Post not found!"

def get_post_reactions(post_id):
    for post in posts:
        if post["id"] == post_id:
            return post["reactions"]
    return "Post not found!"

print(react_to_post("john", 1, "Like"))
print(react_to_post("jane", 1, "Love"))
print(react_to_post("bob", 1, "Haha"))
print(react_to_post("jane", 1, "Wow"))

print("Post reactions:", get_post_reactions(1))