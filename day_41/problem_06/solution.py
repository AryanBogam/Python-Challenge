def count_total_forks(repositories):
    total_forks = 0
    for repo in repositories:
        forks = repo["forks"]
        total_forks += forks
    return total_forks

repositories = [
    {"name": "web-framework", "forks": 45},
    {"name": "mobile-app", "forks": 23},
    {"name": "data-tool", "forks": 67}
]
result = count_total_forks(repositories)
print(result)

repositories2 = [
    {"name": "react-library", "forks": 120},
    {"name": "python-script", "forks": 34},
    {"name": "game-project", "forks": 89},
    {"name": "ml-model", "forks": 56}
]
result2 = count_total_forks(repositories2)
print(result2)