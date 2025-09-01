def left_rotate(nums, k):
    n = len(nums)
    k = k % n
    return nums[k:] + nums[:k]

nums = [1, 2, 3, 4, 5]
k = 2
result = left_rotate(nums, k)
print(result)