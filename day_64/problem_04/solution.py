def longest_increasing_subarray(nums):
    if not nums:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    
    return max_length

nums = [1, 2, 2, 4, 5]
result = longest_increasing_subarray(nums)
print(result)