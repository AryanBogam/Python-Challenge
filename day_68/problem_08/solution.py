def max_sliding_window(nums, k):
    result = []
    
    for i in range(len(nums) - k + 1):
        window_max = nums[i]
        for j in range(i, i + k):
            if nums[j] > window_max:
                window_max = nums[j]
        result.append(window_max)
    
    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = max_sliding_window(nums, k)
print(result)