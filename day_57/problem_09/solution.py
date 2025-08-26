rows = 3
cols = 3

for i in range(rows):
    line = ""
    for j in range(cols):
        if (i + j) % 2 == 0:
            line = line + "*"
        else:
            line = line + "#"
    print(line)