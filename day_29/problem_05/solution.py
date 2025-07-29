nested = [[1, 2], [3, 4], [5]]

flattened = []
for sublist in nested:
    for item in sublist:
        flattened.append(item)

print(flattened)