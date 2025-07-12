def flatten(lst):
    result = []
    stack = list(lst)
    while stack:
        top = stack.pop(0)
        if isinstance(top, list):
            stack = top + stack
        else:
            result.append(top)
    return result

print(flatten([1, [2, [3, 4], 5], 6])) 
