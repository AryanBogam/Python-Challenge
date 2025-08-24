def print_pattern(n):
    for i in range(1, n + 1):
        stars = ""
        for j in range(i):
            stars = stars + "*"
        print(stars)

print_pattern(5)