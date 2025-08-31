def find_subarrays(nums, target):
    result = []
    
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == target:
                result.append(nums[i:j+1])
    
    return result

nums = [1, 2, 3, 4, 2]
target = 5
result = find_subarrays(nums, target)
print(result)