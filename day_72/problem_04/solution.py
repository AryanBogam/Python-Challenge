posts = [
    {"id": 1, "author": "john", "content": "Hello World!", "likes": 15, "comments": 5},
    {"id": 2, "author": "jane", "content": "Great day!", "likes": 8, "comments": 3},
    {"id": 3, "author": "bob", "content": "Learning Python", "likes": 25, "comments": 10},
    {"id": 4, "author": "alice", "content": "Good morning", "likes": 5, "comments": 1}
]

def calculate_popularity_score(post):
    return post["likes"] + (post["comments"] * 2)

def get_trending_posts(limit=5):
    sorted_posts = []
    
    for post in posts:
        post_with_score = post.copy()
        post_with_score["popularity_score"] = calculate_popularity_score(post)
        sorted_posts.append(post_with_score)
    
    for i in range(len(sorted_posts)):
        for j in range(len(sorted_posts) - 1):
            if sorted_posts[j]["popularity_score"] < sorted_posts[j + 1]["popularity_score"]:
                sorted_posts[j], sorted_posts[j + 1] = sorted_posts[j + 1], sorted_posts[j]
    
    return sorted_posts[:limit]

def get_most_liked_posts(limit=3):
    sorted_posts = posts.copy()
    
    for i in range(len(sorted_posts)):
        for j in range(len(sorted_posts) - 1):
            if sorted_posts[j]["likes"] < sorted_posts[j + 1]["likes"]:
                sorted_posts[j], sorted_posts[j + 1] = sorted_posts[j + 1], sorted_posts[j]
    
    return sorted_posts[:limit]

trending = get_trending_posts(3)
most_liked = get_most_liked_posts(2)

print("Trending Posts:")
for post in trending:
    print(f"{post['author']}: {post['content']} (Score: {post['popularity_score']})")

print("\nMost Liked Posts:")
for post in most_liked:
    print(f"{post['author']}: {post['content']} (Likes: {post['likes']})")