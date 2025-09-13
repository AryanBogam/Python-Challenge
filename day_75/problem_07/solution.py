videos = [
    {"id": 1, "title": "My First Vlog", "author": "Aryan"},
    {"id": 2, "title": "Cooking Tutorial", "author": "Chef"}
]

playlists = {"user1": {"favorites": [1, 2]}}
history = {"user1": [1, 2]}

def delete_video(video_id, username):
    for video in videos:
        if video["id"] == video_id:
            if video["author"] == username:
                videos.remove(video)
                
                for user in playlists:
                    for playlist_name in playlists[user]:
                        if video_id in playlists[user][playlist_name]:
                            playlists[user][playlist_name].remove(video_id)
                
                for user in history:
                    if video_id in history[user]:
                        history[user].remove(video_id)
                
                return "Video deleted!"
            else:
                return "You can only delete your own videos!"
    return "Video not found"

result = delete_video(1, "Aryan")
print(result)
print(videos)
print(playlists)
print(history)