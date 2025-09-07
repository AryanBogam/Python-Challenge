def countSubstrings(s):
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    result = 0
    
    for i in range(len(s)):
        result += expand_around_center(i, i)
        result += expand_around_center(i, i + 1)
    
    return result

s = "abc"
result = countSubstrings(s)
print(result)