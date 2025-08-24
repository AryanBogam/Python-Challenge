def fibonacci(n):
    fib_list = []
    a = 0
    b = 1
    for i in range(n):
        if i == 0:
            fib_list.append(a)
        elif i == 1:
            fib_list.append(b)
        else:
            c = a + b
            fib_list.append(c)
            a = b
            b = c
    return fib_list

result = fibonacci(7)
print(result)