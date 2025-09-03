def find_multiple_intersection(lists):
    if not lists:
        return []
    
    result = []
    first_list = lists[0]
    
    for num in first_list:
        found_in_all = True
        for i in range(1, len(lists)):
            if num not in lists[i]:
                found_in_all = False
                break
        
        if found_in_all and num not in result:
            result.append(num)
    
    return result

lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
result = find_multiple_intersection(lists)
print(result)