posts = [
    {"id": 1, "content": "Beautiful sunset today!", "likes": 0, "comments": []},
    {"id": 2, "content": "Working on my Python skills", "likes": 0, "comments": []}
]

while True:
    print("1. View posts")
    print("2. Like post")
    print("3. Comment on post")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        for post in posts:
            print("Post", post["id"] + ":", post["content"])
            print("Likes:", post["likes"])
            print("Comments:")
            for comment in post["comments"]:
                print("  -", comment)
            print()
    
    elif choice == "2":
        post_id = int(input("Enter post ID to like: "))
        for post in posts:
            if post["id"] == post_id:
                post["likes"] = post["likes"] + 1
                print("Post liked!")
                break
    
    elif choice == "3":
        post_id = int(input("Enter post ID to comment: "))
        comment = input("Enter your comment: ")
        for post in posts:
            if post["id"] == post_id:
                post["comments"].append(comment)
                print("Comment added!")
                break
    
    elif choice == "4":
        break