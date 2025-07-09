def fibonacci_series(n):
    # Condition for negative numbers
    if n <= 0:
        print("Please enter a positive number")
        return
    
    # Condition for number 1
    if n == 1:
        print("Fibonacci Series: 0")
        return
    
    # Start with first two numbers
    a, b = 0, 1
    print("Fibonacci Series:")
    print(a, end=" ")
    print(b, end=" ")
    
    # Generate remaining numbers
    for i in range(2, n):
        next_num = a + b
        print(next_num, end=" ")
        a, b = b, next_num
    print()

n = int(input("Enter number: "))
fibonacci_series(n)

# This problem was feeling difficult for me so took help of chatgpt and understood the concept.