def extract_hashtags(tweet):
    words = tweet.split()
    hashtags = []
    
    for word in words:
        if word.startswith("#"):
            hashtags.append(word)
    
    return hashtags

tweet = "Check out #Python and #AI today!"
hashtags = extract_hashtags(tweet)

print(f"Tweet: {tweet}")
print(f"Hashtags: {hashtags}")