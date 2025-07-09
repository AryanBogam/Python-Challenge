# Method 1: Using a new list and backward iteration
def reverse_list_method(original_list):

    reversed_list = []
    
    # Iterate through the original list from last to first
    for i in range(len(original_list) - 1, -1, -1):
        reversed_list.append(original_list[i])
    
    return reversed_list

# Display the final answer.
print(reverse_list_method([1, 2, 3, 4, 5]))