def count_words_no_urls(tweet):
    words = tweet.split()
    word_count = 0
    
    for word in words:
        if not word.startswith("http"):
            word_count += 1
    
    return word_count

tweet = "Check this https://x.com out!"
word_count = count_words_no_urls(tweet)

print(f"Tweet: {tweet}")
print(f"Word count (excluding URLs): {word_count}")