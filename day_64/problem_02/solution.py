def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transpose = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)
    
    return transpose

matrix = [[1, 2, 3], [4, 5, 6]]
result = transpose_matrix(matrix)

for row in result:
    print(*row)