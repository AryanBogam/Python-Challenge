n = int(input("Enter odd number: "))

for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i) 