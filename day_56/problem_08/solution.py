points = [(1, 2), (3, 4)]
zoom = 1

if zoom == 1:
    grid_size = 6
else:
    grid_size = 4

for y in range(grid_size, 0, -1):
    row = ""
    for x in range(grid_size):
        if (x, y) in points:
            row = row + "X "
        else:
            row = row + ". "
    print(row)