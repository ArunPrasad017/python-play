def dfs(board,i,j,word):
    if not word:
        return True
    if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j]!=word[0]:
        return False
    temp = board[i][j]
    board[i][j] = ' '
    found = dfs(board,i+1,j,word[1:]) or dfs(board,i-1,j,word[1:]) or dfs(board,i,j-1,word[1:]) or dfs(board,i,j+1,word[1:])
    board[i][j] = temp
    return found

def exist(board, word):
    A = len(board)
    B = len(board[0])
    for i in range(A):
        for j in range(B):
            if dfs(board,i,j,word):
                return True
    return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = 'ABCCED'
print(exist(board,word))