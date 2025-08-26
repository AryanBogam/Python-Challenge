rows = 3

for i in range(rows, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    
    line = ""
    for j in range(spaces):
        line = line + " "
    for j in range(stars):
        line = line + "*"
    
    print(line)