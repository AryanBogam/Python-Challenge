rows = 3
cols = 9

for i in range(rows):
    line = ""
    for j in range(cols):
        if (i + j) % 4 == 0:
            line = line + "*"
        else:
            line = line + " "
    print(line)