"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

if n =3

Output:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Hint: Uses the backtracking functionality
"""
import pytest
def generateParenthesis(n):
    res = []
    backtrack(res, "", opened=0,closed=0,size=n)
    return res

def backtrack(res,string,opened,closed,size):
    if len(string)==size*2:
        res.append(string)
    if opened<size:
        backtrack(res, string+'(', opened+1,closed,size)
    if closed<opened:
        backtrack(res,string+')',opened,closed+1,size)

n = 2
print(generateParenthesis(n))

