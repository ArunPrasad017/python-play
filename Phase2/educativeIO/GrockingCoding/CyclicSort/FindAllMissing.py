def find_missing_numbers(nums):
    missingNumbers = []
    # TODO: Write your code here
    i,n=0,len(nums)
    while i<n:
        j=nums[i]-1
        if nums[j]==nums[i]:
            i+=1
        else:
            nums[i],nums[j]=nums[j],nums[i]
    for i in range(n):
        if nums[i]-1!=i:
            missingNumbers.append(i+1)
    return missingNumbers

def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))

if __name__ == "__main__":
    main()