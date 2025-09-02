def is_balanced(s):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack:
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

s = "([{}])"
result = is_balanced(s)
print(result)