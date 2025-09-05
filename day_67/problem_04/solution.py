def find_missing_chars(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    missing = []
    
    for letter in alphabet:
        if letter not in s:
            missing.append(letter)
    
    return missing

s = "hello world"
result = find_missing_chars(s)
print(result)