def count_language_usage(repositories):
    language_count = {}
    for repo in repositories:
        language = repo["language"]
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1
    return language_count

repositories = [
    {"name": "web-app", "language": "JavaScript"},
    {"name": "api-server", "language": "Python"},
    {"name": "mobile-app", "language": "JavaScript"},
    {"name": "data-script", "language": "Python"},
    {"name": "website", "language": "HTML"},
    {"name": "ml-model", "language": "Python"}
]
result = count_language_usage(repositories)
print("Language Usage Statistics:")
for language, count in result.items():
    print(f"{language}: {count} repos")

repositories2 = [
    {"name": "game", "language": "C++"},
    {"name": "web-service", "language": "Java"},
    {"name": "script", "language": "Python"},
    {"name": "app", "language": "Java"}
]
result2 = count_language_usage(repositories2)
print("\nAnother test:")
for language, count in result2.items():
    print(f"{language}: {count} repos")