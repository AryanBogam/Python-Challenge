def is_sublist(small, large):
    if len(small) > len(large):
        return False
    
    for i in range(len(large) - len(small) + 1):
        match = True
        for j in range(len(small)):
            if large[i + j] != small[j]:
                match = False
                break
        if match:
            return True
    
    return False

small = [2, 3]
large = [1, 2, 3, 4]
result = is_sublist(small, large)
print(result)