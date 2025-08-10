def show_commit_history(commits):
    for i in range(len(commits) - 1, -1, -1):
        print(commits[i])

commits = [
    "Initial commit",
    "Add user authentication",
    "Fix login bug",
    "Update documentation",
    "Add new feature"
]

print("Commit History (Most Recent First):")
show_commit_history(commits)

def get_reversed_commits(commits):
    reversed_commits = []
    for i in range(len(commits) - 1, -1, -1):
        reversed_commits.append(commits[i])
    return reversed_commits

result = get_reversed_commits(commits)
print("\nReversed commits list:")
print(result)