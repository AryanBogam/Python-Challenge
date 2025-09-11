users = {
    "john": {"email": "john@email.com", "badges": [], "posts": 0, "comments": 0, "likes_received": 0},
    "jane": {"email": "jane@email.com", "badges": [], "posts": 0, "comments": 0, "likes_received": 0},
    "bob": {"email": "bob@email.com", "badges": [], "posts": 0, "comments": 0, "likes_received": 0}
}

badge_criteria = {
    "First Post": {"posts": 1},
    "Prolific Poster": {"posts": 10},
    "Popular Poster": {"likes_received": 100},
    "Conversationalist": {"comments": 50},
    "Social Butterfly": {"comments": 25, "posts": 5},
    "Rising Star": {"likes_received": 50}
}

def check_and_award_badges(username):
    if username not in users:
        return "User not found!"
    
    user = users[username]
    new_badges = []
    
    for badge_name, criteria in badge_criteria.items():
        if badge_name not in user["badges"]:
            earned = True
            for stat, required in criteria.items():
                if user[stat] < required:
                    earned = False
                    break
            
            if earned:
                user["badges"].append(badge_name)
                new_badges.append(badge_name)
    
    return new_badges

def increment_user_stat(username, stat, amount=1):
    if username in users:
        users[username][stat] += amount
        return check_and_award_badges(username)
    return []

def create_post_with_badges(username, content):
    new_badges = increment_user_stat(username, "posts", 1)
    result = "Post created!"
    if new_badges:
        result += f" New badges earned: {', '.join(new_badges)}"
    return result

def add_comment_with_badges(username, comment):
    new_badges = increment_user_stat(username, "comments", 1)
    result = "Comment added!"
    if new_badges:
        result += f" New badges earned: {', '.join(new_badges)}"
    return result

def receive_likes_with_badges(username, likes_count):
    new_badges = increment_user_stat(username, "likes_received", likes_count)
    result = f"Received {likes_count} likes!"
    if new_badges:
        result += f" New badges earned: {', '.join(new_badges)}"
    return result

def get_user_badges(username):
    if username not in users:
        return "User not found!"
    return users[username]["badges"]

def get_user_stats(username):
    if username not in users:
        return "User not found!"
    
    user = users[username]
    return {
        "posts": user["posts"],
        "comments": user["comments"],
        "likes_received": user["likes_received"],
        "badges": len(user["badges"])
    }

print(create_post_with_badges("john", "My first post!"))
print(receive_likes_with_badges("john", 60))

for i in range(8):
    add_comment_with_badges("john", f"Comment {i+1}")

print("John's badges:", get_user_badges("john"))
print("John's stats:", get_user_stats("john"))