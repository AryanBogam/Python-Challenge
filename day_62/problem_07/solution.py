def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
result = check_anagram(str1, str2)
print(result)