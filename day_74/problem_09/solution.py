videos = [
    {"id": 1, "title": "My First Vlog", "author": "Aryan", "views": 5},
    {"id": 2, "title": "Cooking Tutorial", "author": "Chef", "views": 15},
    {"id": 3, "title": "Travel Vlog", "author": "Traveler", "views": 8}
]

history = {"user1": [1, 2], "user2": [1]}

def get_recommendations(username):
    watched_videos = history.get(username, [])
    recommendations = []
    for video in videos:
        if video["id"] not in watched_videos:
            recommendations.append(video)
    return recommendations

recommendations = get_recommendations("user1")
print(recommendations)