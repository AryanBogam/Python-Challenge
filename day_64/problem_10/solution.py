def is_monotonic(nums):
    if len(nums) <= 1:
        return True
    
    increasing = True
    decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            decreasing = False
        if nums[i] < nums[i-1]:
            increasing = False
    
    return increasing or decreasing

nums = [1, 2, 2, 3]
result = is_monotonic(nums)
print(result)