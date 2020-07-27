def findDisappearedNumbers(nums):
    set1= set(nums)
    return [num for num in range(1,len(nums)+1) if num not in set1]

lst = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(lst))