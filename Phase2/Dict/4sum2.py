def fourSumCount(A, B, C, D):
    res_dict={}
    cnt = 0
    for a in A:
        for b in B:
            if (a+b) not in res_dict:
                res_dict[a+b] = 1
            else:
                res_dict[a+b]+= 1
    for c in C:
        for d in D:
            if -(c+d) in res_dict:
                cnt+=res_dict[-(c+d)]
    return cnt

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(fourSumCount(A,B,C,D))

A= [-1,-1]
B= [-1,1]
C= [-1,1]
D= [1,-1]
print(fourSumCount(A,B,C,D))