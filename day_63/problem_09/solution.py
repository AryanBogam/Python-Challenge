def find_intersection_point(list1, list2):
    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                return num1
    return None

list1 = [1, 3, 5, 7]
list2 = [2, 3, 6, 7]
result = find_intersection_point(list1, list2)
print(result)