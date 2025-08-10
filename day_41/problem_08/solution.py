def check_repo_activity(days_since_commit):
    if days_since_commit <= 7:
        return "Active"
    else:
        return "Inactive"

result = check_repo_activity(3)
print(result)

result2 = check_repo_activity(10)
print(result2)

result3 = check_repo_activity(7)
print(result3)

def detailed_repo_activity(days_since_commit):
    if days_since_commit <= 7:
        return f"Active (last commit {days_since_commit} days ago)"
    else:
        return f"Inactive (last commit {days_since_commit} days ago)"

print("\nDetailed results:")
result4 = detailed_repo_activity(2)
print(result4)

result5 = detailed_repo_activity(15)
print(result5)