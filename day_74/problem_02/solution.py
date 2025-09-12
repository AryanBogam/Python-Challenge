videos = [{"id": 1, "title": "My First Vlog", "author": "Aryan", "views": 4}]

def watch_video(video_id):
    for video in videos:
        if video["id"] == video_id:
            video["views"] += 1
            return f"Video watched! Total views: {video['views']}"
    return "Video not found"

result = watch_video(1)
print(result)