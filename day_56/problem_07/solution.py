import math

current = (0, 0)
locations = [(1, 1), (2, 2), (5, 5)]

max_distance = 0
farthest_point = None

for location in locations:
    distance = math.sqrt((location[0] - current[0])**2 + (location[1] - current[1])**2)
    if distance > max_distance:
        max_distance = distance
        farthest_point = location

print(farthest_point)