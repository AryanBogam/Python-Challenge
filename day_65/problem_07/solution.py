def boundary_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total = 0
    
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                total += matrix[i][j]
    
    return total

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = boundary_sum(matrix)
print(result)