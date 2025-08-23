users = [{"name":"A","age":17},{"name":"B","age":20}]

adult_names = []
for user in users:
    if user["age"] > 18:
        adult_names.append(user["name"])

print(adult_names)