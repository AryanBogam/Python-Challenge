def calculate_average_rating(ratings):
    total = sum(ratings)
    average = total / len(ratings)
    return average

ratings = [5, 4, 4, 5]
result = calculate_average_rating(ratings)
print(result)

print(calculate_average_rating([5, 5, 5, 5]))
print(calculate_average_rating([3, 4, 2, 5, 1]))
print(calculate_average_rating([4, 4, 4]))
print(calculate_average_rating([1, 2, 3, 4, 5]))