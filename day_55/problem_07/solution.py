def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

matrix = [[1, 2, 3], [4, 5, 6]]
result = transpose_matrix(matrix)
print(result)