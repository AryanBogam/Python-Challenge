def row_sums(matrix):
    sums = []
    
    for row in matrix:
        row_sum = 0
        for num in row:
            row_sum += num
        sums.append(row_sum)
    
    return sums

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = row_sums(matrix)
print(result)