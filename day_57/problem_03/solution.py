rows = 4

for i in range(rows, 0, -1):
    line = ""
    for j in range(i):
        line = line + "*"
    print(line)