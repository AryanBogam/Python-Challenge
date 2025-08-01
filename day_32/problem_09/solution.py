def compare_followers(username1, username2, follower_data):
    try:
        followers1 = follower_data[username1]
        followers2 = follower_data[username2]
        
        if followers1 > followers2:
            return f"{username1} is more popular with {followers1} followers"
        elif followers2 > followers1:
            return f"{username2} is more popular with {followers2} followers"
        else:
            return f"Both {username1} and {username2} have equal followers: {followers1}"
            
    except KeyError as e:
        return f"User not found: {e}"

followers = {
    "@elon": 150000000,
    "@elonmusk": 120000000,
    "@python": 5000000
}

comparisons = [
    ("@elon", "@python"),
    ("@elon", "@unknown"),
    ("@python", "@elonmusk")
]

print("FOLLOWER COMPARISON BOT")
print("-" * 30)

for user1, user2 in comparisons:
    result = compare_followers(user1, user2, followers)
    print(f"{user1} vs {user2}: {result}")
    print()