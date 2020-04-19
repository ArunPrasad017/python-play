
def sortArrayByParity(A):
    # solution1: TC- O(n) and SC - O(n)
    # arr =[]
        
    # for i in range(0,len(A)):
    #     if A[i]%2==0:
    #         arr.append(A[i])
        
    # for i in range(0,len(A)):
    #     if A[i]%2!=0:
    #         arr.append(A[i])
    # return arr

    # solution2: using double pointers
    i, j = 0, len(A)-1

    while i<j:
        if (A[i]%2 >A[j]%2):
            A[i],A[j] = A[j],A[i]
                
        if A[i]%2==0:
            i+=1
        if A[j]%2==1:
            j-=1
    return A

A = [1,3,2,4]
sortArrayByParity(A)