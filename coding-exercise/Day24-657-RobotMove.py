"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. 
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. 
Valid moves are R (right), L (left), U (up), and D (down). 
If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
"""

def judgeCircle(moves):
    origin = [0,0]
    for c in moves:
        if c=='U':
            origin[0]+=1
        elif c=='D':
            origin[0]-=1
        elif c=='R':
            origin[1]+=1
        elif c=='L':
            origin[1]-=1
    if origin[0]==0 and origin[1]==0:
        return True
    else:
        return False

string = "RRDD"
print(judgeCircle(string))