users_friends = {
    "Alice": {"Bob", "Charlie"},
    "Bob": {"Alice", "Dave"},
    "Charlie": {"Alice", "Eve"},
    "Dave": {"Bob"},
    "Eve": {"Charlie"}
}

while True:
    print("1. View friends")
    print("2. Get friend recommendations")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        username = input("Enter username: ")
        if username in users_friends:
            print("Friends of", username + ":")
            for friend in users_friends[username]:
                print("-", friend)
        else:
            print("User not found!")
    
    elif choice == "2":
        username = input("Enter username: ")
        if username in users_friends:
            user_friends = users_friends[username]
            recommendations = set()
            
            for friend in user_friends:
                if friend in users_friends:
                    for friend_of_friend in users_friends[friend]:
                        if friend_of_friend != username and friend_of_friend not in user_friends:
                            recommendations.add(friend_of_friend)
            
            print("Friend recommendations for", username + ":")
            for rec in recommendations:
                print("-", rec)
        else:
            print("User not found!")
    
    elif choice == "3":
        break