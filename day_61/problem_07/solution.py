def find_index(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
target = 30
result = find_index(numbers, target)
print(result)