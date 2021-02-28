def isValidSudoku(board):
    rows =[]; cols=[]; squares=[]

    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == '.':
                continue
            val=int(1<<(board[i][j]))