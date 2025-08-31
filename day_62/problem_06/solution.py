def find_pairs(nums, target):
    pairs = []
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    
    return pairs

nums = [1, 2, 3, 4, 5]
target = 6
result = find_pairs(nums, target)
print(result)