def find_max_sum_row(matrix):
    max_sum = 0
    max_row_index = 0
    
    for i in range(len(matrix)):
        row_sum = 0
        for num in matrix[i]:
            row_sum += num
        
        if i == 0 or row_sum > max_sum:
            max_sum = row_sum
            max_row_index = i
    
    return max_row_index

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = find_max_sum_row(matrix)
print(result)