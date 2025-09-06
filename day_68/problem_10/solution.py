def longest_increasing_path(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    memo = {}
    
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        max_path = 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                max_path = max(max_path, 1 + dfs(x, y))
        
        memo[(i, j)] = max_path
        return max_path
    
    result = 0
    for i in range(rows):
        for j in range(cols):
            result = max(result, dfs(i, j))
    
    return result

matrix = [[9,9,4],[6,6,8],[2,1,1]]
result = longest_increasing_path(matrix)
print(result)