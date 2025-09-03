def remove_element(nums, element):
    result = []
    
    for num in nums:
        if num != element:
            result.append(num)
    
    return result

nums = [1, 2, 3, 2, 4]
element = 2
result = remove_element(nums, element)
print(result)