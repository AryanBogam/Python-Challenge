def get_merged_pull_requests(pull_requests):
    merged_prs = []
    
    for pr in pull_requests:
        if pr["merged"] == True:
            merged_prs.append(pr["title"])
    
    return merged_prs

pull_requests = [
    {"title": "Add login feature", "merged": True},
    {"title": "Fix bug in checkout", "merged": False},
    {"title": "Update README", "merged": True},
    {"title": "Refactor code", "merged": False},
    {"title": "Add tests", "merged": True}
]
result = get_merged_pull_requests(pull_requests)
print(result)

pull_requests2 = [
    {"title": "New API endpoint", "merged": True},
    {"title": "CSS improvements", "merged": False},
    {"title": "Security patch", "merged": True}
]
result2 = get_merged_pull_requests(pull_requests2)
print(result2)