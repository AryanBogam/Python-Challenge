def upper_triangle_sum(matrix):
    n = len(matrix)
    total = 0
    
    for i in range(n):
        for j in range(n):
            if j >= i:
                total += matrix[i][j]
    
    return total

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = upper_triangle_sum(matrix)
print(result)