def count_distinct(nums):
    distinct = []
    
    for num in nums:
        if num not in distinct:
            distinct.append(num)
    
    return len(distinct)

nums = [1, 2, 3, 2, 1, 4, 5, 4]
result = count_distinct(nums)
print(result)