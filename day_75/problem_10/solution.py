videos = [
    {"id": 1, "title": "Video 1", "author": "Aryan", "comments": [{"author": "user1", "text": "Great!"}], "likes": ["user1", "user2"]},
    {"id": 2, "title": "Video 2", "author": "Chef", "comments": [{"author": "Aryan", "text": "Nice!"}], "likes": ["Aryan"]}
]

def get_most_active_user():
    user_activity = {}
    
    for video in videos:
        author = video["author"]
        if author not in user_activity:
            user_activity[author] = 0
        user_activity[author] += 1
        
        for comment in video["comments"]:
            commenter = comment["author"]
            if commenter not in user_activity:
                user_activity[commenter] = 0
            user_activity[commenter] += 1
        
        for liker in video["likes"]:
            if liker not in user_activity:
                user_activity[liker] = 0
            user_activity[liker] += 1
    
    most_active = max(user_activity, key=user_activity.get)
    return most_active, user_activity[most_active]

user, activity_count = get_most_active_user()
print(f"Most active user: {user} with {activity_count} activities")