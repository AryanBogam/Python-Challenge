users = {
    "john": {"email": "john@email.com"},
    "jane": {"email": "jane@email.com"},
    "bob": {"email": "bob@email.com"},
    "alice": {"email": "alice@email.com"},
    "charlie": {"email": "charlie@email.com"}
}
friends = {
    "john": ["jane", "bob"],
    "jane": ["john", "alice"],
    "bob": ["john", "charlie"],
    "alice": ["jane"],
    "charlie": ["bob"]
}
groups = {
    "python_lovers": ["john", "alice", "charlie"],
    "book_club": ["jane", "bob", "alice"]
}

def get_mutual_friends_suggestions(username):
    if username not in users:
        return "User not found!"
    
    suggestions = {}
    user_friends = friends.get(username, [])
    
    for friend in user_friends:
        friend_friends = friends.get(friend, [])
        for mutual in friend_friends:
            if mutual != username and mutual not in user_friends:
                if mutual not in suggestions:
                    suggestions[mutual] = 0
                suggestions[mutual] += 1
    
    suggestion_list = []
    for person, count in suggestions.items():
        suggestion_list.append((person, count))
    
    for i in range(len(suggestion_list)):
        for j in range(len(suggestion_list) - 1):
            if suggestion_list[j][1] < suggestion_list[j + 1][1]:
                suggestion_list[j], suggestion_list[j + 1] = suggestion_list[j + 1], suggestion_list[j]
    
    return [person for person, count in suggestion_list[:3]]

def get_group_based_suggestions(username):
    if username not in users:
        return "User not found!"
    
    suggestions = set()
    user_friends = set(friends.get(username, []))
    
    for group_name, members in groups.items():
        if username in members:
            for member in members:
                if member != username and member not in user_friends:
                    suggestions.add(member)
    
    return list(suggestions)

def get_random_suggestions(username, limit=2):
    if username not in users:
        return "User not found!"
    
    user_friends = set(friends.get(username, []))
    suggestions = []
    
    for other_user in users:
        if other_user != username and other_user not in user_friends:
            suggestions.append(other_user)
            if len(suggestions) >= limit:
                break
    
    return suggestions

def get_friend_suggestions(username):
    if username not in users:
        return "User not found!"
    
    mutual_suggestions = get_mutual_friends_suggestions(username)
    group_suggestions = get_group_based_suggestions(username)
    random_suggestions = get_random_suggestions(username, 2)
    
    all_suggestions = set(mutual_suggestions + group_suggestions + random_suggestions)
    return list(all_suggestions)[:5]

print("Mutual friend suggestions for john:", get_mutual_friends_suggestions("john"))
print("Group-based suggestions for john:", get_group_based_suggestions("john"))
print("All suggestions for john:", get_friend_suggestions("john"))