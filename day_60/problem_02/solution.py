friends = []

while True:
    print("1. Add friend")
    print("2. Remove friend")
    print("3. View friends")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        friend_name = input("Enter friend's name: ")
        friends.append(friend_name)
        print("Friend added!")
    
    elif choice == "2":
        friend_name = input("Enter friend's name to remove: ")
        if friend_name in friends:
            friends.remove(friend_name)
            print("Friend removed!")
        else:
            print("Friend not found!")
    
    elif choice == "3":
        print("Your friends:")
        for friend in friends:
            print("-", friend)
        print("Total friends:", len(friends))
    
    elif choice == "4":
        break