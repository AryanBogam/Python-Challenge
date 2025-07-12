def is_valid_sudoku(board):
    for i in range(9):
        row = [c for c in board[i] if c != '.']
        if len(set(row)) != len(row):
            return False
        col = [board[r][i] for r in range(9) if board[r][i] != '.']
        if len(set(col)) != len(col):
            return False
    for box_i in range(3):
        for box_j in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    val = board[box_i*3 + i][box_j*3 + j]
                    if val != '.':
                        block.append(val)
            if len(set(block)) != len(block):
                return False
    return True
