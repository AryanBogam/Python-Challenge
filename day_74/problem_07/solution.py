history = {}

def add_to_history(username, video_id):
    if username not in history:
        history[username] = []
    history[username].append(video_id)
    return f"Video {video_id} added to {username}'s history"

add_to_history("user1", 1)
add_to_history("user1", 2)
add_to_history("user2", 1)
print(history)