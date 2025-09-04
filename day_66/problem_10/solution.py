def is_palindrome_number(n):
    if n < 0:
        return False
    
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    return original == reversed_num

n = 121
result = is_palindrome_number(n)
print(result)