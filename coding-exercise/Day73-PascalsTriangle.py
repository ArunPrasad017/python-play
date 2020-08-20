"""
118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, N: int) -> List[List[int]]:
        res = []
        if N==0:
            return res
        for level in range(N):
            if len(res)==level:
                res.append([])
            level_length = len(res)
            i=level_length-1
            for j in range(level_length):
                if j in [0, level_length - 1]:
                    res[level].append(1)
                else:
                    res[level].append(res[i-1][j-1] + res[i-1][j])
        return res