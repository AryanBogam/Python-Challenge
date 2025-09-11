logged_in_users = ["john", "jane", "bob"]
posts = [
    {"id": 1, "author": "john", "content": "Beautiful sunset!", "comments": []}
]
comment_id_counter = 1

def add_comment(username, post_id, comment_text):
    global comment_id_counter
    if username not in logged_in_users:
        return "Please log in first!"
    
    for post in posts:
        if post["id"] == post_id:
            comment = {
                "id": comment_id_counter,
                "author": username,
                "text": comment_text,
                "replies": []
            }
            post["comments"].append(comment)
            comment_id_counter += 1
            return "Comment added!"
    
    return "Post not found!"

def reply_to_comment(username, post_id, comment_id, reply_text):
    global comment_id_counter
    if username not in logged_in_users:
        return "Please log in first!"
    
    for post in posts:
        if post["id"] == post_id:
            for comment in post["comments"]:
                if comment["id"] == comment_id:
                    reply = {
                        "id": comment_id_counter,
                        "author": username,
                        "text": reply_text
                    }
                    comment["replies"].append(reply)
                    comment_id_counter += 1
                    return "Reply added!"
    
    return "Comment or post not found!"

def get_post_comments(post_id):
    for post in posts:
        if post["id"] == post_id:
            return post["comments"]
    return "Post not found!"

def display_comments(post_id):
    comments = get_post_comments(post_id)
    if isinstance(comments, str):
        return comments
    
    result = []
    for comment in comments:
        result.append(f"{comment['author']}: {comment['text']}")
        for reply in comment["replies"]:
            result.append(f"  -> {reply['author']}: {reply['text']}")
    
    return result

print(add_comment("jane", 1, "Amazing photo!"))
print(add_comment("bob", 1, "Love the colors!"))
print(reply_to_comment("john", 1, 1, "Thank you Jane!"))
print(reply_to_comment("jane", 1, 1, "You're welcome!"))

comments_display = display_comments(1)
for comment in comments_display:
    print(comment)