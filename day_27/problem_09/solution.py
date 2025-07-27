def factorial(n):
    try:
        n = int(n)
        if n < 0:
            return "Invalid input"
        
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result
    except ValueError:
        return "Invalid input"

print(factorial(5))
print(factorial("five"))