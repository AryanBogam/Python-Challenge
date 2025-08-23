students = [("A",80),("B",95),("C",60)]

total = 0
highest_score = 0
topper = ""

for name, score in students:
    total = total + score
    if score > highest_score:
        highest_score = score
        topper = name

average = total / len(students)

print("Average =", round(average, 1))
print("Topper =", topper)