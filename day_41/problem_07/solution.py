def format_contributors(contributors):
    sorted_contributors = sorted(contributors)
    print("Contributors (Alphabetical Order):")
    for contributor in sorted_contributors:
        print(f"- {contributor}")
    return sorted_contributors

contributors = ["John", "Alice", "Bob", "Zoe", "Charlie"]
result = format_contributors(contributors)

print("\nSorted list:", result)

contributors2 = ["Maria", "David", "Anna", "Kevin"]
result2 = format_contributors(contributors2)
print("\nAnother sorted list:", result2)