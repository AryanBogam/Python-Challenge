# The given list in the question.
number_list = [1, 3, 5, 7, 9]

# Converting to tuple.
number_tuple = tuple(number_list)

# Adding 11 by creating a new tuple
new_tuple = number_tuple + (11,)


print("Original list:", number_list)
print("Converted tuple:", number_tuple)
print("New tuple with 11:", new_tuple)
print("Original tuple unchanged:", number_tuple)