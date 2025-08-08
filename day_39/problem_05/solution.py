def count_media_types(media_list):
    photos = 0
    videos = 0
    documents = 0
    for media in media_list:
        if media == "photo":
            photos += 1
        elif media == "video":
            videos += 1
        elif media == "document":
            documents += 1
    return f"Photos: {photos}, Videos: {videos}, Documents: {documents}"

media_list = ["photo", "photo", "video", "photo", "document", "photo", "video", "photo"]
result = count_media_types(media_list)
print(result)

media_list2 = ["video", "document", "photo", "photo", "document"]
result2 = count_media_types(media_list2)
print(result2)