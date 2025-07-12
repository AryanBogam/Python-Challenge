def rotate_list(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2))
