videos = [
    {"id": 1, "title": "My First Vlog", "likes": ["user1", "user2"], "dislikes": ["user3"]},
    {"id": 2, "title": "Cooking Tutorial", "likes": ["user1"], "dislikes": ["user2", "user3"]}
]

def get_dislike_percentage(video_id):
    for video in videos:
        if video["id"] == video_id:
            likes_count = len(video["likes"])
            dislikes_count = len(video["dislikes"])
            total_reactions = likes_count + dislikes_count
            
            if total_reactions == 0:
                return 0
            
            percentage = (dislikes_count / total_reactions) * 100
            return round(percentage, 2)
    return "Video not found"

percentage = get_dislike_percentage(1)
print(f"Dislike percentage: {percentage}%")