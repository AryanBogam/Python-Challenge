def find_union(list1, list2):
    result = []
    
    for num in list1:
        if num not in result:
            result.append(num)
    
    for num in list2:
        if num not in result:
            result.append(num)
    
    return result

list1 = [1, 2, 3]
list2 = [3, 4, 5]
result = find_union(list1, list2)
print(result)