users = [("a", 5), ("b", 12), ("c", 7)]

max_likes = 0
most_active = ""

for user, likes in users:
    if likes > max_likes:
        max_likes = likes
        most_active = user

print(most_active)