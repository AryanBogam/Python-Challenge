def search_autocomplete(partial_input, suggestions):
    """Returns autocomplete suggestions based on partial input"""
    partial_lower = partial_input.lower()
    matches = []
    
    for suggestion in suggestions:
        if suggestion.lower().startswith(partial_lower):
            matches.append(suggestion)
    
    return sorted(matches)

suggestions = ["machine learning", "machinery", "macro"]
result = search_autocomplete("mach", suggestions)
print(result)