def extract_hashtags(post):
    """
    Helper function to extract hashtags from a single post
    """
    hashtags = []
    words = post.split()
    
    for word in words:
        if word.startswith('#'):
            clean_hashtag = word.strip('.,!?;:')
            hashtags.append(clean_hashtag)
    
    return hashtags

def count_trending_hashtags(posts):
    """
    Counts how many times each hashtag appears across all posts
    """
    hashtag_count = {}
    for post in posts:
        hashtags = extract_hashtags(post)
        
        for hashtag in hashtags:
            if hashtag in hashtag_count:
                hashtag_count[hashtag] += 1
            else:
                hashtag_count[hashtag] = 1
    
    return hashtag_count

def get_top_trending(posts, top_n=3):
    """
    Gets the top N trending hashtags
    """
    hashtag_count = count_trending_hashtags(posts)
    sorted_hashtags = sorted(hashtag_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_hashtags[:top_n]

posts = [
    "Loving #Python and #AI today!",
    "Learning #MachineLearning and #Python",
    "Great day for #Coding and #AI",
    "#Python is amazing! #Coding all day",
    "Working on #AI project with #MachineLearning"
]

print("Posts:")
for i, post in enumerate(posts, 1):
    print(f"{i}. {post}")

print("\n" + "="*50)

all_hashtags = count_trending_hashtags(posts)
print("All hashtag counts:")
for hashtag, count in all_hashtags.items():
    print(f"  {hashtag}: {count} times")

print("\n" + "="*50)

top_3 = get_top_trending(posts, 3)
print("Top 3 Trending Hashtags:")
for i, (hashtag, count) in enumerate(top_3, 1):
    print(f"  {i}. {hashtag} ({count} times)")

print("\n" + "="*50)

more_posts = [
    "Good morning! #MondayMotivation #Work",
    "Coffee time #Coffee #Morning",
    "Back to #Work after lunch #MondayMotivation",
    "Need more #Coffee! #Work is tough",
    "Finally done with #Work! #Coffee helped",
    "#MondayMotivation got me through the day!"
]

print("More posts example:")
top_trending = get_top_trending(more_posts, 4)
print("Top Trending Hashtags:")
for i, (hashtag, count) in enumerate(top_trending, 1):
    print(f"  {i}. {hashtag} ({count} times)")