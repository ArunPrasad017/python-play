def permutation(nums):
    nums= sorted(nums)
    res = []
    path = []
    status = [False]* len(nums)
    dfs(nums,res,path,status)
    return res

def dfs(nums,res,path,status):
    if len(nums) == len(path):
        res.append(path[:])
        return
    for i in range(len(nums)):
        if not status[i]:
            if i>0 and nums[i]==nums[i-1] and status[i-1]!=True:
                continue
            status[i] = True
            path.append(nums[i])
            dfs(nums,res,path,status)
            path.pop()
            status[i] = False


lst = [3,3,0,3]
print(permutation(lst))