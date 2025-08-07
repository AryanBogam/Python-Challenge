def get_bitmoji_users(users):
    bitmoji_users = []
    for user in users:
        if user["bitmoji"] == True:
            bitmoji_users.append(user["username"])
    return bitmoji_users

users = [
    {"username": "arya", "bitmoji": True},
    {"username": "zoe", "bitmoji": False},
    {"username": "milan", "bitmoji": True}
]

result = get_bitmoji_users(users)
print(result)