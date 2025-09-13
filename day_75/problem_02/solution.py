videos = [
    {"id": 1, "title": "My First Vlog", "author": "Aryan", "likes": ["user1", "user2"]},
    {"id": 2, "title": "Cooking Tutorial", "author": "Chef", "likes": ["user1", "user2", "user3"]},
    {"id": 3, "title": "Tech Review", "author": "TechGuy", "likes": ["user1"]}
]

def get_top_liked_videos(n):
    sorted_videos = sorted(videos, key=lambda x: len(x["likes"]), reverse=True)
    return sorted_videos[:n]

top_videos = get_top_liked_videos(2)
print(top_videos)