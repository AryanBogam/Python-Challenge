def rank_posts(posts):

    # Calculate scores for each post
    for post in posts:
        post['score'] = 3 * post['likes'] + 5 * post['comments'] + 10 * post['shares']
    
    # Sort by score in descending order and return top 3
    sorted_posts = sorted(posts, key=lambda x: x['score'], reverse=True)
    return sorted_posts[:3]

posts = [
    {"id": 1, "likes": 10, "comments": 5, "shares": 2},
    {"id": 2, "likes": 20, "comments": 10, "shares": 5},
    {"id": 3, "likes": 5, "comments": 15, "shares": 1},
    {"id": 4, "likes": 30, "comments": 3, "shares": 8}
]

top_posts = rank_posts(posts)
for post in top_posts:
    print(f"Post {post['id']}: Score = {post['score']}")