for num in range(1, 1001):
    divisor_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    
    if divisor_sum == num:
        print(f"{num} is a perfect number")