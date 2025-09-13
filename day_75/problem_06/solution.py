videos = [
    {"id": 1, "title": "My First Vlog", "author": "Aryan", "description": "This is my first vlog!"},
    {"id": 2, "title": "Cooking Tutorial", "author": "Chef", "description": "Learn to cook pasta"}
]

def update_description(video_id, new_description):
    for video in videos:
        if video["id"] == video_id:
            video["description"] = new_description
            return "Description updated!"
    return "Video not found"

update_description(1, "This is my updated first vlog with new content!")
print(videos[0]["description"])