def are_disjoint(list1, list2):
    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                return False
    return True

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = are_disjoint(list1, list2)
print(result)