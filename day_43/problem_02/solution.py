def extract_hashtags(post):
    """
    Finds all hashtags (words starting with #) in a post
    """
    hashtags = []
    words = post.split()
    
    for word in words:
        if word.startswith('#'):
            clean_hashtag = word.strip('.,!?;:')
            hashtags.append(clean_hashtag)
    return hashtags

post1 = "Loving #Python and #AI"
hashtags1 = extract_hashtags(post1)
print(f'Post: "{post1}"')
print(f"Hashtags found: {hashtags1}")
print("\n" + "="*50)

post2 = "Just learned #MachineLearning! #DataScience is amazing. #TechLife"
hashtags2 = extract_hashtags(post2)
print(f'Post: "{post2}"')
print(f"Hashtags found: {hashtags2}")

print("\n" + "="*50)

post3 = "No hashtags in this post at all!"
hashtags3 = extract_hashtags(post3)
print(f'Post: "{post3}"')
print(f"Hashtags found: {hashtags3}")
print("\n" + "="*50)

post4 = "#MondayMotivation #Work #Success! Let's go #Team."
hashtags4 = extract_hashtags(post4)
print(f'Post: "{post4}"')
print(f"Hashtags found: {hashtags4}")
print("\n" + "="*50)

post5 = "Starting my day with #Coffee, going to #Work, ending with #Netflix"
hashtags5 = extract_hashtags(post5)
print(f'Post: "{post5}"')
print(f"Hashtags found: {hashtags5}")