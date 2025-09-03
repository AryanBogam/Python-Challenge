def has_unique_characters(s):
    seen = []
    
    for char in s:
        if char in seen:
            return False
        seen.append(char)
    
    return True

s = "abcde"
result = has_unique_characters(s)
print(result)