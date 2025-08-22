followers1 = ["a", "b", "c"]
followers2 = ["b", "c", "d"]

mutual = []
for follower in followers1:
    if follower in followers2:
        mutual.append(follower)

print(mutual)