def find_common_interests(users):
    pairs = []
    user_list = list(users.keys())
    
    for i in range(len(user_list)):
        for j in range(i + 1, len(user_list)):
            user1 = user_list[i]
            user2 = user_list[j]
            
            common = set(users[user1]) & set(users[user2])
            
            if len(common) >= 3:
                pairs.append((user1, user2))
    
    return pairs

users = {
    1: ["coding", "music", "travel", "food"],
    2: ["coding", "music", "travel", "books"],
    3: ["gaming", "art", "movies", "dance"]
}

print(find_common_interests(users))