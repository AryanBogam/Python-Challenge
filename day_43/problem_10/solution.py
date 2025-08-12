def calculate_engagement_score(likes, comments, reposts):
    """
    Calculates engagement score using the formula:
    score = likes*1 + comments*2 + reposts*3
    """
    score = (likes * 1) + (comments * 2) + (reposts * 3)
    return score

def calculate_post_engagement(post):
    """
    Calculates engagement score for a post dictionary
    """
    likes = post.get('likes', 0)
    comments = post.get('comments', 0)
    reposts = post.get('reposts', 0)
    
    score = calculate_engagement_score(likes, comments, reposts)

    post_with_score = post.copy()
    post_with_score['engagement_score'] = score
    
    return post_with_score

def rank_posts_by_engagement(posts):
    """
    Sorts posts by engagement score (highest first)
    """
    posts_with_scores = []
    for post in posts:
        post_with_score = calculate_post_engagement(post)
        posts_with_scores.append(post_with_score)

    ranked_posts = sorted(posts_with_scores, key=lambda x: x['engagement_score'], reverse=True)
    
    return ranked_posts

def display_engagement_breakdown(post):
    """
    Shows detailed engagement breakdown for a post
    """
    likes = post.get('likes', 0)
    comments = post.get('comments', 0)
    reposts = post.get('reposts', 0)
    score = post.get('engagement_score', 0)
    
    print(f"Post: \"{post['content']}\"")
    print(f" Likes: {likes} × 1 = {likes}")
    print(f" Comments: {comments} × 2 = {comments * 2}")
    print(f" Reposts: {reposts} × 3 = {reposts * 3}")
    print(f" Total Engagement Score: {score}")

# Example usage
print("ENGAGEMENT SCORE CALCULATOR")
print("="*50)
print("Formula: Likes×1 + Comments×2 + Reposts×3")
print()

# Test individual calculations
likes1, comments1, reposts1 = 10, 5, 2
score1 = calculate_engagement_score(likes1, comments1, reposts1)
print(f"Example 1: {likes1} likes, {comments1} comments, {reposts1} reposts")
print(f"Score: {likes1}×1 + {comments1}×2 + {reposts1}×3 = {score1}")

print("\n" + "="*50)

posts = [
    {
        "content": "Just launched my new app!",
        "likes": 45,
        "comments": 12,
        "reposts": 8,
        "user": "john"
    },
    {
        "content": "Beautiful sunset today",
        "likes": 23,
        "comments": 6,
        "reposts": 3,
        "user": "sarah"
    },
    {
        "content": "Learning Python programming! #Python",
        "likes": 18,
        "comments": 15,
        "reposts": 5,
        "user": "mike"
    },
    {
        "content": "Coffee and coding",
        "likes": 31,
        "comments": 4,
        "reposts": 2,
        "user": "anna"
    }
]

print("INDIVIDUAL POST ENGAGEMENT:")
print("-"*50)
for post in posts:
    post_with_score = calculate_post_engagement(post)
    display_engagement_breakdown(post_with_score)
    print()

print("="*50)

ranked_posts = rank_posts_by_engagement(posts)

print("POSTS RANKED BY ENGAGEMENT:")
print("-"*50)
for i, post in enumerate(ranked_posts, 1):
    print(f"{i}. Score: {post['engagement_score']} - @{post['user']}")
    print(f"   \"{post['content']}\"")
    print(f"   {post['likes']} {post['comments']} {post['reposts']}")
    print()

print("="*50)

top_post = ranked_posts[0]
print("TOP PERFORMING POST:")
display_engagement_breakdown(top_post)

print("\n" + "="*50)

total_engagement = sum(post['engagement_score'] for post in ranked_posts)
average_engagement = total_engagement / len(ranked_posts)

print("ENGAGEMENT ANALYTICS:")
print(f"Total posts analyzed: {len(posts)}")
print(f"Total engagement points: {total_engagement}")
print(f"Average engagement per post: {average_engagement:.1f}")
print(f"Highest engagement: {ranked_posts[0]['engagement_score']}")
print(f"Lowest engagement: {ranked_posts[-1]['engagement_score']}")