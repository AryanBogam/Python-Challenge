list_a = [1, 2, 3, 4, 5]
list_b = [2, 3]

difference = []
for item in list_a:
    if item not in list_b:
        difference.append(item)

print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Items in A but not in B: {difference}")