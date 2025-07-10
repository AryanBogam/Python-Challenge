# Given tuple
tup = (10, 20, 30, 40, 50)

# Convert to list and modify
lst = list(tup)
lst.append(60)
lst.remove(20)

# Convert back to tuple
tup = tuple(lst)
print(tup)
