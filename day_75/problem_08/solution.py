history = {"user1": [1, 2, 3, 4, 5]}

def get_recently_watched(username, n):
    if username in history:
        recent_videos = history[username][-n:]
        return list(reversed(recent_videos))
    return []

recent = get_recently_watched("user1", 3)
print(recent)