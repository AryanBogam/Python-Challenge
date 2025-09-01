def find_triplets(nums, target):
    result = []
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    result.append((nums[i], nums[j], nums[k]))
    
    return result

nums = [1, 2, 3, 4, 5]
target = 9
result = find_triplets(nums, target)
print(result)