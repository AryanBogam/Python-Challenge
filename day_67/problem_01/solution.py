def insert_element(nums, element, index):
    result = []
    
    for i in range(len(nums) + 1):
        if i == index:
            result.append(element)
        if i < len(nums):
            result.append(nums[i])
    
    return result

nums = [10, 20, 40]
element = 30
index = 2
result = insert_element(nums, element, index)
print(result)