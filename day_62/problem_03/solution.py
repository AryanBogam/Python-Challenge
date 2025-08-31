def move_zeros(nums):
    result = []
    zeros = []
    
    for num in nums:
        if num == 0:
            zeros.append(num)
        else:
            result.append(num)
    
    return result + zeros

nums = [0, 1, 0, 3, 12]
result = move_zeros(nums)
print(result)