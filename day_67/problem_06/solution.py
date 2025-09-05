def longest_common_prefix(words):
    if not words:
        return ""
    
    prefix = ""
    min_len = len(words[0])
    
    for word in words:
        if len(word) < min_len:
            min_len = len(word)
    
    for i in range(min_len):
        char = words[0][i]
        
        for word in words:
            if word[i] != char:
                return prefix
        
        prefix += char
    
    return prefix

words = ["flower", "flow", "flight"]
result = longest_common_prefix(words)
print(result)