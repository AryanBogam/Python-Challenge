def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_substring(s):
    longest = ""
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    
    return longest

s = "babad"
result = longest_palindromic_substring(s)
print(result)