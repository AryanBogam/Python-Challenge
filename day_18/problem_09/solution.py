search_terms = {}

def track_search(keyword):
    keyword = keyword.lower()
    search_terms[keyword] = search_terms.get(keyword, 0) + 1

track_search("Azure")
track_search("azure")
track_search("GitHub Copilot")
print(search_terms)
