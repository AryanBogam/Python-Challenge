videos = [
    {"id": 1, "title": "My First Vlog", "comments": [
        {"author": "user1", "text": "Great video!", "likes": []},
        {"author": "user2", "text": "Nice work!", "likes": []}
    ]}
]

def like_comment(video_id, comment_index, username):
    for video in videos:
        if video["id"] == video_id:
            if comment_index < len(video["comments"]):
                comment = video["comments"][comment_index]
                if username not in comment["likes"]:
                    comment["likes"].append(username)
                    return "Comment liked!"
                else:
                    comment["likes"].remove(username)
                    return "Comment unliked!"
    return "Video or comment not found"

like_comment(1, 0, "user3")
like_comment(1, 0, "user4")
print(videos[0]["comments"][0]["likes"])