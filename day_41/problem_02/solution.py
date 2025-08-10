def find_most_popular_repo(repositories):
    most_popular = ""
    highest_stars = 0
    for repo in repositories:
        name = repo["name"]
        stars = repo["stars"]
        if stars > highest_stars:
            highest_stars = stars
            most_popular = name
    return most_popular

repositories = [
    {"name": "my-project", "stars": 120},
    {"name": "web-app", "stars": 245},
    {"name": "python-tool", "stars": 89}
]
result = find_most_popular_repo(repositories)
print(result)

repositories2 = [
    {"name": "game-engine", "stars": 500},
    {"name": "chat-app", "stars": 300},
    {"name": "calculator", "stars": 150}
]
result2 = find_most_popular_repo(repositories2)
print(result2)