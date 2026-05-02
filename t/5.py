# Branch and Bound Solution: N-Queens Problem

def solve_nqueens_bb(n):
    board = [[0]*n for _ in range(n)]

    col = [False]*n
    diag1 = [False]*(2*n)  # row - col
    diag2 = [False]*(2*n)  # row + col

    def solve(row):
        if row == n:
            return True

        for c in range(n):
            if not col[c] and not diag1[row-c+n] and not diag2[row+c]:
                board[row][c] = 1
                col[c] = diag1[row-c+n] = diag2[row+c] = True

                if solve(row + 1):
                    return True

                # Backtrack
                board[row][c] = 0
                col[c] = diag1[row-c+n] = diag2[row+c] = False

        return False

    if solve(0):
        print("Solution (Branch & Bound):")
        for row in board:
            print(row)
    else:
        print("No solution exists")


# ---------------- Main ----------------
solve_nqueens_bb(4)