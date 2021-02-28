def rotate(nums,k):
    def reverse(n,start,end):
        while start<end:
            n[start], n[end] = n[end], n[start]
            start+=1
            end-=1
        return n
    n = len(nums)
    k%=n
    reverse(nums,0,n-1)
    reverse(nums, 0,k-1)
    reverse(nums, k,n-1)
    return nums


nums = [1,2,3,4,5,6,7]
print(rotate(nums,3))