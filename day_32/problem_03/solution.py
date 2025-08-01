def track_mentions(tweets):
    mention_count = {}
    
    for tweet in tweets:
        words = tweet.split()
        for word in words:
            if word.startswith("@"):
                if word not in mention_count:
                    mention_count[word] = 0
                mention_count[word] += 1
    
    return mention_count

tweets = ["@elon", "thanks @elon", "hi @ai"]
mentions = track_mentions(tweets)

print("Tweets:", tweets)
print("Mention counts:", mentions)