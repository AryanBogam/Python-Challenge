pinned_tweet = None

def pin_tweet(tweet):
    global pinned_tweet
    old_tweet = pinned_tweet
    pinned_tweet = tweet
    
    if old_tweet:
        print(f"Replaced pinned tweet: '{old_tweet}'")
    
    print(f"New pinned tweet: '{tweet}'")

def show_pinned_tweet():
    if pinned_tweet:
        print(f"Current pinned tweet: '{pinned_tweet}'")
    else:
        print("No tweet is currently pinned")

print("PINNED TWEET MANAGER")
print("-" * 30)

pin_tweet("Hello World! This is my first tweet!")
show_pinned_tweet()

print()
pin_tweet("Learning Python is awesome! #Python")
show_pinned_tweet()