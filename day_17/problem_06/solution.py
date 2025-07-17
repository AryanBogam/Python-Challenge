def highlight_keywords(post, keywords):
    result = post
    for keyword in keywords:
        result = result.replace(keyword, f"*{keyword}*")
    return result

post = "I love coding and programming"
keywords = ["coding", "programming"]

print(highlight_keywords(post, keywords))