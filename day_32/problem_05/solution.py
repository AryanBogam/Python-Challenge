def find_trending_hashtags(tweets):
    hashtag_count = {}

    for tweet in tweets:
        words = tweet.split()
        for word in words:
            if word.startswith("#"):
                if word not in hashtag_count:
                    hashtag_count[word] = 0
                hashtag_count[word] += 1

    sorted_hashtags = sorted(hashtag_count.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_hashtags[:3]
    
    return top_3

tweets = [
    "Love #Python and #AI",
    "#Python is great!",
    "#AI and #ML are trending",
    "#Python rocks!"
]

trending = find_trending_hashtags(tweets)
print("Sample tweets:", tweets)
print("Top 3 trending hashtags:")
for i, (hashtag, count) in enumerate(trending, 1):
    print(f"{i}. {hashtag}: {count} times")