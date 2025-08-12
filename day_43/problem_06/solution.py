def calculate_total_likes(posts):
    """
    Calculates the total number of likes across all posts
    Each post should have a 'likes' field
    """
    total_likes = 0
    for post in posts:
        total_likes += post['likes']
    return total_likes

def find_most_liked_post(posts):
    """
    Finds the post with the most likes
    """
    if not posts:
        return None
    most_liked = posts[0]
    for post in posts:
        if post['likes'] > most_liked['likes']:
            most_liked = post
    
    return most_liked

def display_post_stats(posts):
    """
    Shows detailed statistics about posts and likes
    """
    print("POST ENGAGEMENT STATS")
    print("="*40)

    for i, post in enumerate(posts, 1):
        print(f"{i}. \"{post['content']}\" - {post['likes']} likes")
    
    print("\n" + "-"*40)

    total = calculate_total_likes(posts)
    print(f"Total likes across all posts: {total}")

    top_post = find_most_liked_post(posts)
    if top_post:
        print(f"Most liked post: \"{top_post['content']}\" ({top_post['likes']} likes)")

    if posts:
        average = total / len(posts)
        print(f"Average likes per post: {average:.1f}")

posts = [
    {"content": "Good morning everyone! #MondayMotivation", "likes": 15},
    {"content": "Just learned Python! So excited! #Python", "likes": 42},
    {"content": "Having coffee", "likes": 8},
    {"content": "Check out my new project! #Coding", "likes": 28},
    {"content": "Beautiful sunset today", "likes": 35}
]
display_post_stats(posts)
print("\n" + "="*60)

social_posts = [
    {"content": "My cat is so cute!", "likes": 156},
    {"content": "Rainy day thoughts", "likes": 23},
    {"content": "Best pizza ever!", "likes": 89},
    {"content": "Finished reading a great book!", "likes": 34},
    {"content": "Weekend vibes!", "likes": 67}
]

print("Another example:")
display_post_stats(social_posts)

print("\n" + "="*60)

total_likes = calculate_total_likes(posts)
most_liked = find_most_liked_post(posts)

print("Quick calculations:")
print(f"Total likes: {total_likes}")
print(f"Most liked post: \"{most_liked['content']}\" with {most_liked['likes']} likes")