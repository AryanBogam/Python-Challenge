def find_duplicates(nums):
    count = {}
    duplicates = []
    
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num, freq in count.items():
        if freq > 1:
            duplicates.append(num)
    
    return duplicates

nums = [1, 2, 3, 2, 1, 5]
result = find_duplicates(nums)
print(result)