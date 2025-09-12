videos = [{"id": 1, "title": "My First Vlog", "author": "Aryan", "views": 5, "likes": [], "dislikes": []}]

def like_video(video_id, username):
    for video in videos:
        if video["id"] == video_id:
            if username in video["dislikes"]:
                video["dislikes"].remove(username)
            if username not in video["likes"]:
                video["likes"].append(username)
            return "Video liked!"
    return "Video not found"

def dislike_video(video_id, username):
    for video in videos:
        if video["id"] == video_id:
            if username in video["likes"]:
                video["likes"].remove(username)
            if username not in video["dislikes"]:
                video["dislikes"].append(username)
            return "Video disliked!"
    return "Video not found"

like_video(1, "user1")
dislike_video(1, "user2")
print(videos[0]["likes"])
print(videos[0]["dislikes"])