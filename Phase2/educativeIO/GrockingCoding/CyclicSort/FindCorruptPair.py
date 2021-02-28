def find_corrupt_numbers(nums):
    # TODO: Write your code here
    res = []
    i,n=0,len(nums)
    while i<n:
        j=nums[i]-1
        if nums[i]!=nums[j]:
            nums[i],nums[j] = nums[j], nums[i]
        else:
            i+=1
    for i in range(n):
        if nums[i]-1!=i:
            res.append(nums[i])
            res.append(i+1)
    return res

def main():
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))

if __name__ == "__main__":
    main()
