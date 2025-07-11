def manual_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(manual_max([5, 10, 20, 8]))
