def count_open_issues(issues):
    open_count = 0
    for issue in issues:
        if issue["status"] == "open":
            open_count += 1
    return open_count

issues = [
    {"title": "Bug in login", "status": "open"},
    {"title": "Add new feature", "status": "closed"},
    {"title": "Fix typo", "status": "open"},
    {"title": "Update docs", "status": "closed"},
    {"title": "Security issue", "status": "open"}
]
result = count_open_issues(issues)
print(result)

issues2 = [
    {"title": "Memory leak", "status": "closed"},
    {"title": "UI improvement", "status": "open"},
    {"title": "Database error", "status": "closed"}
]
result2 = count_open_issues(issues2)
print(result2)