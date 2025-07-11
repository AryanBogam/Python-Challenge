def reverse_lst(lst):
    reverse_list = []
    i = 0
    while i < len(lst):
        l = lst.pop()
        reverse_list.append(l)
    return (reverse_list)

print(reverse_lst([1, 2, 3, 4]))