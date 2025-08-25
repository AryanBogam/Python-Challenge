import math

points = [(0, 0), (3, 4), (6, 8)]

total_distance = 0
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    total_distance = total_distance + distance

print(total_distance)