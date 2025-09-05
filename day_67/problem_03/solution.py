def are_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    
    map1 = {}
    map2 = {}
    
    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]
        
        if char1 in map1:
            if map1[char1] != char2:
                return False
        else:
            map1[char1] = char2
        
        if char2 in map2:
            if map2[char2] != char1:
                return False
        else:
            map2[char2] = char1
    
    return True

s1 = "egg"
s2 = "add"
result = are_isomorphic(s1, s2)
print(result)