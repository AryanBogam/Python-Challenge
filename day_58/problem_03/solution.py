rows = 4

for i in range(rows, 0, -1):
    line = ""
    for j in range(1, i + 1):
        line = line + str(j) + " "
    print(line)