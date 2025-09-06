def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            result = []
            for i in range(n):
                row_str = "." * n
                row_str = row_str[:board[i]] + "Q" + row_str[board[i]+1:]
                result.append(row_str)
            solutions.append(result)
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
    
    solutions = []
    backtrack([-1] * n, 0)
    return solutions

n = 4
result = solve_n_queens(n)
for solution in result:
    for row in solution:
        print(row)
    print()