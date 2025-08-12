def check_for_spam(post, blocked_words):
    """
    Checks if a post contains any blocked/spam words
    Returns True if spam is detected, False otherwise
    """
    post_lower = post.lower()
    
    for blocked_word in blocked_words:
        if blocked_word.lower() in post_lower:
            return True, blocked_word
    
    return False, None

def moderate_post(post, blocked_words):
    """
    Moderates a post and returns result with details
    """
    is_spam, spam_word = check_for_spam(post, blocked_words)
    
    result = {
        "post": post,
        "is_spam": is_spam,
        "spam_word": spam_word,
        "status": "BLOCKED" if is_spam else "APPROVED"
    }
    
    return result

def display_moderation_result(result):
    """
    Shows moderation result in a nice format
    """
    post = result["post"]
    status = result["status"]
    
    if result["is_spam"]:
        print(f"{status}: \"{post}\"")
        print(f"   Reason: Contains blocked word '{result['spam_word']}'")
    else:
        print(f"{status}: \"{post}\"")

blocked_words = ["spam", "fake", "scam", "virus", "click here", "free money"]

test_posts = [
    "Good morning everyone! Hope you have a great day!",
    "This is totally fake news, don't believe it!",
    "Click here for free money! Amazing opportunity!",
    "Just finished my coding project. So proud!",
    "Warning: This website might have a virus",
    "Learning Python programming today",
    "Don't fall for this scam, be careful!",
    "Beautiful sunset today"
]

print("CONTENT MODERATION SYSTEM")
print("="*50)
print("Blocked words:", blocked_words)
print()

approved_posts = []
blocked_posts = []

for post in test_posts:
    result = moderate_post(post, blocked_words)
    display_moderation_result(result)
    
    if result["is_spam"]:
        blocked_posts.append(post)
    else:
        approved_posts.append(post)

print("\n" + "="*50)
print("MODERATION SUMMARY:")
print(f"Total posts checked: {len(test_posts)}")
print(f"Approved: {len(approved_posts)}")
print(f"Blocked: {len(blocked_posts)}")

print("\n" + "-"*30)
print("Approved posts:")
for i, post in enumerate(approved_posts, 1):
    print(f"{i}. \"{post}\"")

print("\n" + "-"*30) 
print("Blocked posts:")
for i, post in enumerate(blocked_posts, 1):
    print(f"{i}. \"{post}\"")

print("\n" + "="*50)

custom_blocked = ["bad", "terrible", "worst"]
test_post = "This is the worst product ever! Really bad quality!"

print("Testing with custom blocked words:")
print(f"Blocked words: {custom_blocked}")
print(f"Test post: \"{test_post}\"")

result = moderate_post(test_post, custom_blocked)
display_moderation_result(result)