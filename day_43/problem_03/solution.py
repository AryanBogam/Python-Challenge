def extract_mentions(post):
    """
    Finds all mentions (words starting with @) in a post
    """
    mentions = []
    words = post.split()
    
    for word in words:
        if word.startswith('@'):
            clean_mention = word.strip('.,!?;:')
            mentions.append(clean_mention)
    
    return mentions

post1 = "Thanks @John and @Sara"
mentions1 = extract_mentions(post1)
print(f'Post: "{post1}"')
print(f"Mentions found: {mentions1}")

print("\n" + "="*50)

post2 = "Hey @Alice! Did you see what @Bob posted? @Charlie would love this!"
mentions2 = extract_mentions(post2)
print(f'Post: "{post2}"')
print(f"Mentions found: {mentions2}")

print("\n" + "="*50)

post3 = "No mentions in this post!"
mentions3 = extract_mentions(post3)
print(f'Post: "{post3}"')
print(f"Mentions found: {mentions3}")

print("\n" + "="*50)

post4 = "Shoutout to @TeamLead, @Developer1, and @Designer2 for the great work!"
mentions4 = extract_mentions(post4)
print(f'Post: "{post4}"')
print(f"Mentions found: {mentions4}")

print("\n" + "="*50)

post5 = "Thanks @John! Hope @Sara, @Mike, and @Lisa see this."
mentions5 = extract_mentions(post5)
print(f'Post: "{post5}"')
print(f"Mentions found: {mentions5}")
print("\n" + "="*50)

def count_mentions(post):
    """
    Returns the number of mentions in a post
    """
    mentions = extract_mentions(post)
    return len(mentions)

print(f"Total mentions in post1: {count_mentions(post1)}")
print(f"Total mentions in post4: {count_mentions(post4)}")