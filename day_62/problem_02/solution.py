def find_intersection(list1, list2):
    result = []
    for num in list1:
        if num in list2 and num not in result:
            result.append(num)
    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = find_intersection(list1, list2)
print(result)