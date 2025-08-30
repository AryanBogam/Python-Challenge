def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum

numbers = [3, 7, 1, 9, 2]
max_val, min_val = find_max_min(numbers)
print("Max:", max_val, "Min:", min_val)