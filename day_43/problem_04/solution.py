def sort_posts_by_time(posts):
    """
    Sorts posts from most recent to oldest based on timestamp
    Each post should be a dictionary with 'content' and 'timestamp'
    """
    sorted_posts = sorted(posts, key=lambda post: post['timestamp'], reverse=True)
    return sorted_posts

def display_feed(posts):
    """
    Shows posts in a nice feed format
    """
    print("📱 FEED (Most Recent First)")
    print("="*40)
    
    for i, post in enumerate(posts, 1):
        print(f"{i}. Time: {post['timestamp']}")
        print(f"   Post: {post['content']}")
        print()

posts = [
    {"content": "Good morning everyone! #MondayMotivation", "timestamp": 1000},
    {"content": "Just had lunch! #FoodLover", "timestamp": 1500},
    {"content": "Starting my day with coffee", "timestamp": 800},
    {"content": "Working late tonight #Coding", "timestamp": 2000},
    {"content": "Time for bed! Good night", "timestamp": 2200}
]

print("Original posts (unsorted):")
for i, post in enumerate(posts, 1):
    print(f"{i}. Time: {post['timestamp']} - {post['content']}")
print("\n" + "="*50)
sorted_posts = sort_posts_by_time(posts)

print("Sorted feed:")
display_feed(sorted_posts)
print("="*50)

more_posts = [
    {"content": "Breakfast time!", "timestamp": 900},
    {"content": "Afternoon snack", "timestamp": 1400},
    {"content": "Evening workout", "timestamp": 1900},
    {"content": "Morning jog", "timestamp": 700},
    {"content": "Lunch break!", "timestamp": 1200}
]

print("Another feed example:")
sorted_more_posts = sort_posts_by_time(more_posts)
display_feed(sorted_more_posts)