marks = (45, 91, 85, 95, 76)

high_indexes = []
for i in range(len(marks)):
    if marks[i] > 90:
        high_indexes.append(i)

print(high_indexes)