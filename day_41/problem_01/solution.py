def count_total_stars(repositories):
    total_stars = 0
    for repo in repositories:
        stars = repo["stars"]
        total_stars += stars
    return total_stars

repositories = [
    {"name": "my-project", "stars": 120},
    {"name": "web-app", "stars": 45},
    {"name": "python-tool", "stars": 89}
]
result = count_total_stars(repositories)
print(result)

repositories2 = [
    {"name": "react-app", "stars": 200},
    {"name": "node-api", "stars": 150},
    {"name": "mobile-app", "stars": 75}
]
result2 = count_total_stars(repositories2)
print(result2)