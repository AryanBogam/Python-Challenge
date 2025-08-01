def categorize_sentiment(tweet):
    positive_words = ["love", "great", "awesome"]
    negative_words = ["hate", "bad", "terrible"]
    
    words = tweet.lower().split()
    for word in words:
        if word in positive_words:
            return "positive"

    for word in words:
        if word in negative_words:
            return "negative"
    
    return "neutral"

test_tweets = [
    "I love Python programming!",
    "This is terrible and bad",
    "Just had lunch today"
]

for tweet in test_tweets:
    sentiment = categorize_sentiment(tweet)
    print(f"Tweet: '{tweet}' → Sentiment: {sentiment}")