videos = [
    {"id": 1, "title": "My First Vlog", "author": "Aryan", "views": 5},
    {"id": 2, "title": "Cooking Tutorial", "author": "Chef", "views": 15},
    {"id": 3, "title": "Travel Vlog", "author": "Traveler", "views": 8}
]

def get_trending_videos():
    trending = sorted(videos, key=lambda x: x["views"], reverse=True)
    return trending

trending_videos = get_trending_videos()
print(trending_videos)