def move_negatives(nums):
    negatives = []
    positives = []
    
    for num in nums:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)
    
    return negatives + positives

nums = [1, -2, 3, -4]
result = move_negatives(nums)
print(result)