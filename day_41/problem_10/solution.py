def search_repositories_by_keyword(repositories, keyword):
    matching_repos = []
    for repo in repositories:
        description = repo["description"].lower()
        keyword_lower = keyword.lower()
        if keyword_lower in description:
            matching_repos.append(repo["name"])
    return matching_repos

repositories = [
    {"name": "todo-app", "description": "A simple web application for managing tasks"},
    {"name": "weather-api", "description": "REST API for weather data"},
    {"name": "task-manager", "description": "Desktop application for task tracking"},
    {"name": "blog-site", "description": "Personal blog web application"},
    {"name": "game-engine", "description": "2D game development framework"}
]

result = search_repositories_by_keyword(repositories, "application")
print(f"Repositories containing 'application': {result}")

result2 = search_repositories_by_keyword(repositories, "web")
print(f"Repositories containing 'web': {result2}")

result3 = search_repositories_by_keyword(repositories, "API")
print(f"Repositories containing 'API': {result3}")

def search_with_count(repositories, keyword):
    matches = search_repositories_by_keyword(repositories, keyword)
    count = len(matches)
    return f"Found {count} repositories containing '{keyword}': {matches}"

result4 = search_with_count(repositories, "task")
print(result4)