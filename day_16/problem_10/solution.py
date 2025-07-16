def rank_search_results(search_results):
    # Sort by click_count in descending order
    sorted_results = sorted(search_results, key=lambda x: x['click_count'], reverse=True)
    
    # Return top 3 results
    return sorted_results[:3]

results = [
    {"title": "Result A", "click_count": 100},
    {"title": "Result B", "click_count": 250},
    {"title": "Result C", "click_count": 50},
    {"title": "Result D", "click_count": 300}
]
top_results = rank_search_results(results)
print([r['title'] for r in top_results])