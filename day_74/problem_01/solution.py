videos = []

def upload_video(title, author):
    video_id = len(videos) + 1
    video = {"id": video_id, "title": title, "author": author, "views": 0}
    videos.append(video)
    return f"Video uploaded successfully! Video ID: {video_id}"

result = upload_video("My First Vlog", "Aryan")
print(result)
print(videos)