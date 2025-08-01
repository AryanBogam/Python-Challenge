class TweetTooLongError(Exception):
    pass

def validate_tweet_length(tweet):
    if len(tweet) > 280:
        raise TweetTooLongError("Tweet exceeds 280 character limit!")
    return True

test_tweets = [
    "Short tweet",
    "This is a very long tweet that definitely exceeds the 280 character limit. " * 5
]

for tweet in test_tweets:
    try:
        validate_tweet_length(tweet)
        print(f"Tweet ({len(tweet)} chars): Valid ✓")
    except TweetTooLongError as e:
        print(f"Tweet ({len(tweet)} chars): {e}")