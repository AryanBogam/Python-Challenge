ratings = [5, 4, 3, 4, 5]

total = 0
for rating in ratings:
    total = total + rating

average = total / len(ratings)
print("Average =", average)