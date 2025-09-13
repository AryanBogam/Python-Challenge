videos = [
    {"id": 1, "title": "My First Vlog", "author": "Aryan", "views": 100, "comments": [{"author": "user1", "text": "Great!"}], "likes": ["user1", "user2"]},
    {"id": 2, "title": "Another Vlog", "author": "Aryan", "views": 50, "comments": [{"author": "user2", "text": "Nice!"}], "likes": ["user3"]}
]

def get_user_summary(username):
    uploaded_videos = 0
    total_views = 0
    comments_made = 0
    likes_given = 0
    
    for video in videos:
        if video["author"] == username:
            uploaded_videos += 1
            total_views += video["views"]
        
        for comment in video["comments"]:
            if comment["author"] == username:
                comments_made += 1
        
        if username in video["likes"]:
            likes_given += 1
    
    return {
        "uploaded_videos": uploaded_videos,
        "total_views": total_views,
        "comments_made": comments_made,
        "likes_given": likes_given
    }

summary = get_user_summary("Aryan")
print(summary)