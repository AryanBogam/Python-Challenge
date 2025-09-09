friends = {
    "aryan": ["alice", "bob", "charlie"],
    "raj": ["bob", "charlie", "diana"],
    "john": ["alice", "eve"],
    "jane": ["charlie", "diana", "eve"]
}

def find_mutual_friends(user1, user2):
    if user1 not in friends or user2 not in friends:
        return "One or both users not found!"
    
    user1_friends = friends[user1]
    user2_friends = friends[user2]
    
    mutual = []
    for friend in user1_friends:
        if friend in user2_friends:
            mutual.append(friend)
    
    return mutual

def count_mutual_friends(user1, user2):
    mutual = find_mutual_friends(user1, user2)
    if isinstance(mutual, str):
        return mutual
    return len(mutual)

def find_common_connections(user_list):
    if len(user_list) < 2:
        return "Need at least 2 users!"
    
    common = friends.get(user_list[0], [])
    
    for user in user_list[1:]:
        if user not in friends:
            return f"User {user} not found!"
        
        new_common = []
        for friend in common:
            if friend in friends[user]:
                new_common.append(friend)
        common = new_common
    
    return common

print("Mutual friends between aryan and raj:", find_mutual_friends("aryan", "raj"))
print("Mutual friends count:", count_mutual_friends("aryan", "raj"))
print("Common friends among aryan, raj, jane:", find_common_connections(["aryan", "raj", "jane"]))