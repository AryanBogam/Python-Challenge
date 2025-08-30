def find_second_largest(numbers):
    largest = numbers[0]
    second_largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

numbers = [5, 2, 8, 1, 9, 3]
result = find_second_largest(numbers)
print(result)