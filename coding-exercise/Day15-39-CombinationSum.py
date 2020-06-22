# Combination Sum
def combinationSum(candidates, target):
    candidates.sort()
    res = []
    lst = []
    dfs(candidates,target,0,lst,res)
    return res

def dfs(candidates,target,start_idx,lst,res):
    if target==0:
        res.append(lst[:])
        return
    for i in range(start_idx,len(candidates)):
        if (candidates[i])>target:
            return

        lst.append(candidates[i])
        dfs(candidates,(target-candidates[i]),i,lst,res)
        lst.pop()

candidates = [8,7,4,3]
target = 11
print(combinationSum(candidates,target))