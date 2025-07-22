Q10. Airspace Conflict Detector

Concepts: Functions, coordinates, distance
Problem:
Two planes are flying with coordinates (x1, y1) and (x2, y2).
If the distance between them is less than 5 km, warn "Risk of collision".

use this formula:
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

Hint: Write a function check_conflict(x1, y1, x2, y2).