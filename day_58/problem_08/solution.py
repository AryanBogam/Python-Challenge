n = 3

for i in range(1, n + 1):
    line = ""
    for j in range(1, n + 1):
        result = i * j
        line = line + str(result) + " "
    print(line)