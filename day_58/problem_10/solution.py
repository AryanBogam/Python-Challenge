rows = 4

for i in range(rows):
    line = ""
    num = 1
    for j in range(i + 1):
        line = line + str(num) + " "
        num = num * (i - j) // (j + 1)
    print(line)