def max_sub_array_of_size_k(k, arr):
# TODO: Write your code here
    sum_val,max_sum,start=0,0,0
    cnt = 0
    for end in range(len(arr)):
        sum_val+=arr[end]
        cnt+=1
        if cnt>=k:
            cnt-=1
            max_sum=max(max_sum,sum_val)
            sum_val-=arr[start]
            start+=1
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k=3 
print(max_sub_array_of_size_k(k,arr))