videos = [{"id": 1, "title": "My First Vlog", "author": "Aryan", "views": 5, "comments": []}]

def add_comment(video_id, author, comment_text):
    for video in videos:
        if video["id"] == video_id:
            comment = {"author": author, "text": comment_text}
            video["comments"].append(comment)
            return "Comment added!"
    return "Video not found"

add_comment(1, "Raj", "Great video!")
add_comment(1, "Sara", "Nice work!")
print(videos[0]["comments"])