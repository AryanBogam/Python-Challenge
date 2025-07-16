def clean_watch_history(video_titles):
    seen = {}
    result = []
    
    for i in range(len(video_titles) - 1, -1, -1):
        title = video_titles[i]
        if title not in seen:
            seen[title] = True
            result.append(title)
    
    # Reverse to maintain original order
    return result[::-1]

videos = ["Video A", "Video B", "Video A", "Video C", "Video B"]
result = clean_watch_history(videos)
print(result)