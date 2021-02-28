"""
LeetCode - 79

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

DFS and backtracking
"""
def dfs(board,i,j,word):
    found = False
    if not word:
        return True
    if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j]!=word[0]:
        return False
    temp = board[i][j]
    board[i][j] = ' '
    found = dfs(board,i-1,j,word[1:]) or dfs(board,i+1,j,word[1:]) or dfs(board,i,j-1,word[1:]) or dfs(board,i,j+1,word[1:])
    board[i][j] = temp
    return found

def exist(board, word):
    a= len(board)
    b= len(board[0])

    for i in range(a):
        for j in range(b):
            if dfs(board, i, j, word):
                return True
    return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"
print(exist(board,word))
