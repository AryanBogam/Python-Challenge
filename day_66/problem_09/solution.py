def max_product_two_numbers(nums):
    max_product = nums[0] * nums[1]
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]
            if product > max_product:
                max_product = product
    
    return max_product

nums = [3, 4, 5, 2]
result = max_product_two_numbers(nums)
print(result)