def find_odd_occurrence(nums):
    count = {}
    
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num, freq in count.items():
        if freq % 2 == 1:
            return num
    
    return None

nums = [1, 2, 3, 2, 3, 1, 3]
result = find_odd_occurrence(nums)
print(result)