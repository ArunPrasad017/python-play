class Solution:
    def generate(self, N: int) -> List[List[int]]:
        res = []
        if N==0:
            return res
        level = 0
        while level<N:
            if len(res)==level:
                res.append([])
            level_length = len(res)
            i=level_length-1
            for j in range(level_length):
                if j==0 or j==level_length-1:
                    res[level].append(1)
                else:
                    res[level].append(res[i-1][j-1] + res[i-1][j])
            level+=1
        return res