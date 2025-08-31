def rotate_list(nums, k):
    n = len(nums)
    k = k % n
    return nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5]
k = 2
result = rotate_list(nums, k)
print(result)