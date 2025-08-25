import math

points = [(0, 0), (1, 1), (10, 10)]
max_distance = 2

clusters = []
used = []

for i in range(len(points)):
    if i not in used:
        cluster = [points[i]]
        used.append(i)
        
        for j in range(len(points)):
            if j not in used:
                distance = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
                if distance <= max_distance:
                    cluster.append(points[j])
                    used.append(j)
        
        clusters.append(cluster)

for i, cluster in enumerate(clusters):
    print("Cluster", i + 1, ":", cluster)