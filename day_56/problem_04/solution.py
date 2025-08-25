locations = [(1, 2), (3, 4), (5, 0)]

min_x = locations[0][0]
max_x = locations[0][0]
min_y = locations[0][1]
max_y = locations[0][1]

for x, y in locations:
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

print("min =", (min_x, min_y), "max =", (max_x, max_y))