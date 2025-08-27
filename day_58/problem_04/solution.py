rows = 3

for i in range(1, rows + 1):
    line = ""
    for j in range(i):
        line = line + "*"
    print(line)

for i in range(rows - 1, 0, -1):
    line = ""
    for j in range(i):
        line = line + "*"
    print(line)