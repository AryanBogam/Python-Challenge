import math

start = (0, 0)
points = [(1, 1), (2, 2), (3, 3)]

route = [start]
remaining = points.copy()
current = start

while remaining:
    nearest = None
    min_distance = float('inf')
    
    for point in remaining:
        distance = math.sqrt((point[0] - current[0])**2 + (point[1] - current[1])**2)
        if distance < min_distance:
            min_distance = distance
            nearest = point
    
    route.append(nearest)
    remaining.remove(nearest)
    current = nearest

route_str = ""
for i, point in enumerate(route):
    route_str = route_str + str(point)
    if i < len(route) - 1:
        route_str = route_str + "->"

print("Route =", route_str)