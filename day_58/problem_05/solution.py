rows = 3

for i in range(1, rows + 1):
    line = ""
    for j in range(1, i + 2):
        line = line + str(j)
        if j <= i:
            line = line + " * "
    print(line)