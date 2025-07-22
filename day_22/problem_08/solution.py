rows = 4

for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()