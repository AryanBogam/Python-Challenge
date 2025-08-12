def get_follow_suggestions(user_follows, all_user_followers, user_name):
    """
    Suggests new accounts to follow based on who your friends follow
    
    user_follows: list of users that the person follows
    all_user_followers: dictionary with each user and their followers list
    user_name: the person we're making suggestions for
    """
    suggestions = []
    

    for friend in user_follows:
        if friend in all_user_followers:
            friends_followers = all_user_followers[friend]
            for potential_follow in friends_followers:
                if (potential_follow != user_name and 
                    potential_follow not in user_follows and 
                    potential_follow not in suggestions):
                    suggestions.append(potential_follow)
    
    return suggestions

def display_suggestions(user_name, user_follows, suggestions):
    """
    Shows follow suggestions in a nice format
    """
    print(f"👥 FOLLOW SUGGESTIONS for @{user_name}")
    print("="*40)
    print(f"You currently follow: {user_follows}")
    print()
    
    if suggestions:
        print("Suggested accounts to follow:")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. @{suggestion}")
    else:
        print("No new suggestions at this time.")

john_follows = ["Alice", "Bob", "Charlie"]

all_followers = {
    "Alice": ["Bob", "Diana", "Eve"],
    "Bob": ["Alice", "Charlie", "Frank"],
    "Charlie": ["Alice", "Diana", "George"],
    "Diana": ["Eve", "Frank", "John"],
    "Eve": ["Alice", "Frank"],
    "Frank": ["Bob", "George"]
}

suggestions = get_follow_suggestions(john_follows, all_followers, "John")
display_suggestions("John", john_follows, suggestions)
print("\n" + "="*50)

sarah_follows = ["Mike", "Lisa"]

all_followers_2 = {
    "Mike": ["Lisa", "Tom", "Anna"],
    "Lisa": ["Mike", "Tom", "David"],
    "Tom": ["Anna", "David", "Sarah"],
    "Anna": ["Mike", "David"],
    "David": ["Tom", "Anna"]
}

suggestions_2 = get_follow_suggestions(sarah_follows, all_followers_2, "Sarah")
display_suggestions("Sarah", sarah_follows, suggestions_2)
print("\n" + "="*50)

alex_follows = ["User1", "User2", "User3"]

big_network = {
    "User1": ["User4", "User5", "User6"],
    "User2": ["User5", "User7", "User8"], 
    "User3": ["User6", "User8", "User9"],
    "User4": ["User1", "User10"],
    "User5": ["User2", "User10"]
}

suggestions_3 = get_follow_suggestions(alex_follows, big_network, "Alex")
display_suggestions("Alex", alex_follows, suggestions_3)
print("\n" + "="*50)

print("HOW SUGGESTIONS WORK:")
print("Step 1: Look at who John follows:", john_follows)
print("Step 2: Check who John's friends follow:")
for friend in john_follows:
    if friend in all_followers:
        print(f"  - {friend} follows: {all_followers[friend]}")
print("Step 3: Suggest people John doesn't follow yet:", suggestions)