rows = 4
cols = 5

for i in range(rows):
    line = ""
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            line = line + "*"
        else:
            line = line + " "
    print(line)