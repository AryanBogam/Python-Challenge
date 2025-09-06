def oranges_rotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = []
    fresh = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    minutes = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        minutes += 1
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx, ny))
    
    return minutes - 1 if fresh == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
result = oranges_rotting(grid)
print(result)