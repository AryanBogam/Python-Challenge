rows = 4

number = 1
for i in range(1, rows + 1):
    line = ""
    for j in range(i):
        line = line + str(number) + " "
        number = number + 1
    print(line)