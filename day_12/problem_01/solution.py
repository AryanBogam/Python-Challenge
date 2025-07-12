def is_sentence_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_sentence_palindrome("A man a plan a canal Panama"))
