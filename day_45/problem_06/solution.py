def filter_suggestions(suggestions, search_word):
    matching_suggestions = []
    
    for suggestion in suggestions:
        if suggestion.startswith(search_word):
            matching_suggestions.append(suggestion)
    return matching_suggestions

suggestions = ["python tutorial", "python code", "java basics"]
search_word = "python"
filtered = filter_suggestions(suggestions, search_word)

print(f'Search word: "{search_word}"')
print(f"All suggestions: {suggestions}")
print(f"Filtered suggestions: {filtered}")

all_suggestions = [
    "python tutorial", 
    "python code", 
    "java basics", 
    "javascript guide",
    "java advanced"
]

test_words = ["python", "java", "javascript", "css"]

for word in test_words:
    results = filter_suggestions(all_suggestions, word)
    print(f'\nSearch "{word}": {results}')

def filter_suggestions_ignore_case(suggestions, search_word):
    matching_suggestions = []
    search_lower = search_word.lower()
    
    for suggestion in suggestions:
        if suggestion.lower().startswith(search_lower):
            matching_suggestions.append(suggestion)
    
    return matching_suggestions

print("\nCase-insensitive search:")
mixed_case = ["Python Tutorial", "PYTHON Code", "Java Basics"]
result = filter_suggestions_ignore_case(mixed_case, "python")
print(f'Search "python": {result}')