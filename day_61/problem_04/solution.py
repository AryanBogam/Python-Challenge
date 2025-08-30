def sum_elements(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_elements(numbers)
print(result)