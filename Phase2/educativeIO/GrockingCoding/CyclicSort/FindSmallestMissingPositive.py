def smallestPositive(nums):
    i,n = 0,len(nums)
    while i<n:
        j = nums[i]-1
        if nums[i]>0 and nums[i]<n and nums[i]!=nums[j]:
            nums[i],nums[j] = nums[j], nums[i]
        else:
            i+=1
    for i in range(n):
        if nums[i]-1!=i:
            return i+1
    return -1

def main():
    nums = [-3, 1, 5, 4, 2]
    print(smallestPositive(nums))
    nums = [3, -2, 0, 1, 2]
    print(smallestPositive(nums))
    nums = [4,3,1,5]
    print(smallestPositive(nums))

if __name__ == "__main__":
    main()