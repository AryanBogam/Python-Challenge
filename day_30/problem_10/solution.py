import math

point1 = (3, 4)
point2 = (7, 1)

x1, y1 = point1
x2, y2 = point2

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Distance: {distance:.2f}")