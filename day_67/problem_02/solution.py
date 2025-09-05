def find_all_indices(nums, target):
    indices = []
    
    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)
    
    return indices

nums = [1, 2, 3, 2, 4, 2]
target = 2
result = find_all_indices(nums, target)
print(result)