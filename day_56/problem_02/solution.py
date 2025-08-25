import math

current = (0, 0)
locations = [(1, 1), (2, 2), (3, 3)]

min_distance = float('inf')
nearest_point = None

for location in locations:
    distance = math.sqrt((location[0] - current[0])**2 + (location[1] - current[1])**2)
    if distance < min_distance:
        min_distance = distance
        nearest_point = location

print(nearest_point)