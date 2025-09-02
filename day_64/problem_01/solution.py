def find_missing_positive(nums):
    positive = 1
    
    while True:
        if positive not in nums:
            return positive
        positive += 1

nums = [3, 4, -1, 1]
result = find_missing_positive(nums)
print(result)