def check_post_length(post):
    """
    Counts characters in a post and checks if it exceeds the limit
    """
    character_count = len(post)
    limit = 500
    if character_count > limit:
        return character_count, True
    else:
        return character_count, False

def display_post_status(post):
    """
    Shows post length status with nice formatting
    """
    count, exceeds_limit = check_post_length(post)
    limit = 500
    print(f"Post length: {count} characters")
    print(f"Limit: {limit} characters")
    
    if exceeds_limit:
        over_by = count - limit
        print(f"Post exceeds limit by {over_by} characters!")
    else:
        remaining = limit - count
        print(f"Post is within limit. {remaining} characters remaining.")

post1 = "This is a short post about Python programming!"
print("Post 1:")
display_post_status(post1)
print("\n" + "="*50)

post2 = "This is a much longer post that talks about many things. " * 10
print("Post 2:")
display_post_status(post2)
print("\n" + "="*50)

post3 = "A" * 500
print("Post 3 (exactly 500 characters):")
display_post_status(post3)
print("\n" + "="*50)

post4 = ""
print("Post 4 (empty):")
display_post_status(post4)