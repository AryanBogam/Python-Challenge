fps = [120, 140, 160]

total = 0
for f in fps:
    total = total + f

average = total / len(fps)
print(average)