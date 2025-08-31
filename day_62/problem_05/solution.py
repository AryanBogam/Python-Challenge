def first_non_repeating(s):
    count = {}
    
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for char in s:
        if count[char] == 1:
            return char
    
    return None

s = "swiss"
result = first_non_repeating(s)
print(result)