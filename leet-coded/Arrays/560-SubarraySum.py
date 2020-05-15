# def subarraysum(nums,n):
#     dict1= {k:v for k,v in enumerate(nums)}
#     cnt = 0
#     i=0
#     while i+1 in dict1.keys():
#         if n == (dict1[i] + dict1[i+1]):
#             cnt+=1
#         i+=1
#     return cnt

def subarraysum(nums,n):
    sum_dict = {0:1}
    count = 0
    sum_val = 0
    for num in nums:
        sum_val+=num
        if (sum_val-n) in sum_dict:
            count+=sum_dict[sum_val-n]
        if sum_val in sum_dict:
            sum_dict[sum_val]+=1
        else:
            sum_dict[sum_val]=1
    return count

nums = [1,2,3]
k = 3
print(subarraysum(nums,k))