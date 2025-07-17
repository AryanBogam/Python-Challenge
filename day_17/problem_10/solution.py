def trending_hashtags(posts):
    hashtag_count = {}
    
    for post in posts:
        words = post.split()
        for word in words:
            if word.startswith('#'):
                hashtag = word.lower()
                hashtag_count[hashtag] = hashtag_count.get(hashtag, 0) + 1
    
    # Sort by count and get top 5
    sorted_hashtags = sorted(hashtag_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_hashtags[:5]

posts = [
    "Love #coding and #python",
    "Great #python tutorial #coding",
    "#coding is fun #tech",
    "New #python project #coding #tech"
]

print(trending_hashtags(posts))