def search_posts(posts, keyword):
    """
    Searches for posts containing a specific keyword
    Returns all matching posts
    """
    matching_posts = []
    
    for post in posts:
        if keyword.lower() in post.lower():
            matching_posts.append(post)
    
    return matching_posts

def search_posts_with_details(posts, keyword):
    """
    Searches posts and returns detailed results with positions
    Each post is a dictionary with content and other details
    """
    matching_posts = []
    
    for post in posts:
        if keyword.lower() in post['content'].lower():
            matching_posts.append(post)
    
    return matching_posts

def display_search_results(posts, keyword, results):
    """
    Shows search results in a nice format
    """
    print(f"SEARCH RESULTS for \"{keyword}\"")
    print("="*50)
    print(f"Searched in {len(posts)} posts")
    print(f"Found {len(results)} matching posts:")
    print()
    
    if results:
        for i, result in enumerate(results, 1):
            print(f"{i}. \"{result}\"")
    else:
        print("No posts found containing the keyword.")

simple_posts = [
    "I love programming with Python!",
    "Just finished my AI project",
    "Coffee and coding go together",
    "Learning machine learning with Python",
    "Beautiful day for outdoor activities",
    "Working on my AI startup idea"
]

keyword = "AI"
results = search_posts(simple_posts, keyword)
display_search_results(simple_posts, keyword, results)

print("\n" + "="*60)

detailed_posts = [
    {"content": "Good morning! Starting my day with Python coding", "likes": 15, "user": "john"},
    {"content": "Just deployed my AI model to production!", "likes": 42, "user": "sarah"},
    {"content": "Coffee break time", "likes": 8, "user": "mike"},
    {"content": "Learning new Python libraries today", "likes": 28, "user": "anna"},
    {"content": "AI is changing everything!", "likes": 35, "user": "david"},
    {"content": "Weekend hiking trip", "likes": 19, "user": "lisa"}
]

def display_detailed_search(posts, keyword, results):
    """
    Shows detailed search results with user and like info
    """
    print(f"🔍 DETAILED SEARCH for \"{keyword}\"")
    print("="*50)
    print(f"Found {len(results)} posts:")
    print()
    
    for i, post in enumerate(results, 1):
        print(f"{i}. User: @{post['user']}")
        print(f"   Post: \"{post['content']}\"")
        print(f"   Likes: {post['likes']}")
        print()

keyword2 = "Python"
detailed_results = search_posts_with_details(detailed_posts, keyword2)
display_detailed_search(detailed_posts, keyword2, detailed_results)

print("="*60)

keywords_to_test = ["AI", "coffee", "weekend", "xyz"]
for test_keyword in keywords_to_test:
    results = search_posts_with_details(detailed_posts, test_keyword)
    print(f"Keyword '{test_keyword}': {len(results)} posts found")