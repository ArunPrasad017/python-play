def longest_subarray(arr,k):
    max_cnt,start,max_ones_cntr = 0,0,0
    for end in range(len(arr)):
        if arr[end]==1:
            max_ones_cntr+=1
        if (end-start+1-max_ones_cntr)>k:
            if arr[start]==1:
                max_ones_cntr-=1
            start+=1
        max_cnt=max(max_cnt,end-start+1)
    return max_cnt

Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k=2
print(longest_subarray(Array,k))

Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k=3
print(longest_subarray(Array,k))