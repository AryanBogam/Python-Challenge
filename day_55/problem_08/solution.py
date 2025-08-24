def is_palindrome(text):
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            return False
    return True

result = is_palindrome("madam")
print(result)