videos = [
    {"id": 1, "title": "My First Vlog", "author": "Aryan Tech"},
    {"id": 2, "title": "Cooking Tutorial", "author": "Chef Master"},
    {"id": 3, "title": "Another Video", "author": "Aryan Tech"}
]

def search_channels(name):
    channels = []
    for video in videos:
        if name.lower() in video["author"].lower():
            if video["author"] not in channels:
                channels.append(video["author"])
    return channels

found_channels = search_channels("Aryan")
print(found_channels)