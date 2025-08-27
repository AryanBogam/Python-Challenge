rows = 3

for i in range(1, rows + 1):
    spaces = rows - i
    line = ""
    
    for j in range(spaces):
        line = line + " "
    
    for j in range(1, i + 1):
        line = line + str(j) + " "
    
    for j in range(i - 1, 0, -1):
        line = line + str(j) + " "
    
    print(line)