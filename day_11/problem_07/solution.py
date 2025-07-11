def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 5, 'c': 9}))
