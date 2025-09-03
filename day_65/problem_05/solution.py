def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    
    for letter in alphabet:
        if letter not in s:
            return False
    
    return True

s = "The quick brown fox jumps over the lazy dog"
result = is_pangram(s)
print(result)