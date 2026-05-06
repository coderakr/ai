def is_safe(board, row, col, n):
    # check column
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    # check left diagonal
    i,j = row-1, col -1
    while i>=0 and j>=0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # check Right diagonal
    i,j = row-1, col+1
    while i>=0 and j<n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def n_queen(board, row, n):
    if row == n:
        return True
        
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col] = 1

            if(n_queen(board,row+1,n)):
                return True
        
        board[row][col] = 0

    return False

n = 4
board = [[0]*n for _ in range(n)]
if(n_queen(board,0,n)):
    print("solution:")
    for row in board:
        print(row)
else:
    print("solution doesn't exist")


     