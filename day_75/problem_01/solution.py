videos = [
    {"id": 1, "title": "My First Vlog", "author": "Aryan", "tags": ["Vlog", "Daily"]},
    {"id": 2, "title": "Cooking Tutorial", "author": "Chef", "tags": ["Tutorial", "Cooking"]},
    {"id": 3, "title": "Tech Review", "author": "TechGuy", "tags": ["Tech", "Review"]}
]

def search_by_tag(tag):
    results = []
    for video in videos:
        if tag in video["tags"]:
            results.append(video)
    return results

tech_videos = search_by_tag("Tech")
print(tech_videos)