def queens(size):
    board = [[0 for x in range(size)] for y in range(size)]
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, size)):
            if board[i][j] == 1:
                return False
        return True

    def solve(row):
        if row == size:
            solution = []
            for r in range(size):
                for c in range(size):
                    if board[r][c] == 1:
                        solution.append(str(c + 1))
            solutions.append(''.join(solution))
        else:
            for col in range(size):
                if is_safe(row, col):
                    board[row][col] = 1
                    solve(row + 1)
                    board[row][col] = 0

    solve(0)
    return sorted(solutions)