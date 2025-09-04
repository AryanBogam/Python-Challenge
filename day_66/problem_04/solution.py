def find_peak_element(nums):
    n = len(nums)
    
    for i in range(n):
        left_ok = (i == 0) or (nums[i] >= nums[i - 1])
        right_ok = (i == n - 1) or (nums[i] >= nums[i + 1])
        
        if left_ok and right_ok:
            return i
    
    return -1

nums = [1, 2, 3, 1]
result = find_peak_element(nums)
print(result)