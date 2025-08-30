def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

numbers = [1, 2, 3, 4, 5]
result = is_sorted(numbers)
print(result)