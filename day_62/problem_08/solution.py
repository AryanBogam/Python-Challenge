def find_majority(nums):
    count = {}
    n = len(nums)
    
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num, freq in count.items():
        if freq > n // 2:
            return num
    
    return None

nums = [3, 3, 4, 2, 3, 3, 5]
result = find_majority(nums)
print(result)