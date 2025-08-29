posts = [
    {"user": "Alice", "content": "Had a great day at the beach!", "likes": 5},
    {"user": "Bob", "content": "Learning Python programming", "likes": 3},
    {"user": "Eve", "content": "Just finished my project", "likes": 8}
]

while True:
    print("1. View news feed")
    print("2. Like a post")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        print("News Feed:")
        for i, post in enumerate(posts):
            print(str(i + 1) + ".", post["user"] + ":", post["content"])
            print("   Likes:", post["likes"])
    
    elif choice == "2":
        try:
            post_num = int(input("Enter post number to like: ")) - 1
            if 0 <= post_num < len(posts):
                posts[post_num]["likes"] = posts[post_num]["likes"] + 1
                print("Post liked!")
            else:
                print("Invalid post number!")
        except:
            print("Invalid input!")
    
    elif choice == "3":
        break