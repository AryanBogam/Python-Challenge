def is_symmetric(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    
    return True

matrix = [[1, 2, 3], [2, 1, 4], [3, 4, 1]]
result = is_symmetric(matrix)
print(result)