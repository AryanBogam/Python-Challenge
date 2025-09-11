posts = [
    {"id": 1, "author": "john", "content": "Going on vacation to the beach this summer", "date": "2023-06-15"},
    {"id": 2, "author": "jane", "content": "Python programming tips for beginners", "date": "2023-06-14"},
    {"id": 3, "author": "bob", "content": "Beautiful sunset at the beach yesterday", "date": "2023-06-13"},
    {"id": 4, "author": "alice", "content": "Learning Python is fun and exciting", "date": "2023-06-12"},
    {"id": 5, "author": "john", "content": "Holiday celebrations with family", "date": "2023-06-11"}
]

def search_posts_by_keyword(keyword):
    keyword = keyword.lower()
    matching_posts = []
    
    for post in posts:
        if keyword in post["content"].lower():
            matching_posts.append(post)
    
    return matching_posts

def search_posts_by_author(author):
    author_posts = []
    
    for post in posts:
        if post["author"].lower() == author.lower():
            author_posts.append(post)
    
    return author_posts

def search_posts_by_date(date):
    date_posts = []
    
    for post in posts:
        if post["date"] == date:
            date_posts.append(post)
    
    return date_posts

def advanced_search(keyword=None, author=None, date=None):
    results = posts.copy()
    
    if keyword:
        keyword = keyword.lower()
        results = [post for post in results if keyword in post["content"].lower()]
    
    if author:
        author = author.lower()
        results = [post for post in results if post["author"].lower() == author]
    
    if date:
        results = [post for post in results if post["date"] == date]
    
    return results

def search_multiple_keywords(keywords):
    matching_posts = []
    
    for post in posts:
        content_lower = post["content"].lower()
        matches_all = True
        
        for keyword in keywords:
            if keyword.lower() not in content_lower:
                matches_all = False
                break
        
        if matches_all:
            matching_posts.append(post)
    
    return matching_posts

def get_search_results_summary(results):
    if not results:
        return "No posts found!"
    
    summary = []
    for post in results:
        summary.append(f"{post['author']}: {post['content'][:50]}...")
    
    return summary

beach_posts = search_posts_by_keyword("beach")
python_posts = search_posts_by_keyword("python")
john_posts = search_posts_by_author("john")

print("Beach posts:", len(beach_posts))
print("Python posts:", len(python_posts))
print("John's posts:", len(john_posts))

advanced_results = advanced_search(keyword="python", author="jane")
print("Advanced search results:", len(advanced_results))

multi_keyword_results = search_multiple_keywords(["python", "learning"])
print("Multi-keyword search:", len(multi_keyword_results))