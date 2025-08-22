users = [("a", 10), ("b", 0), ("c", 5)]

inactive = []
for user, likes in users:
    if likes == 0:
        inactive.append(user)

print(inactive)