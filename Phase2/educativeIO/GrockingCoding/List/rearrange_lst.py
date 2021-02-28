def rearrange(lst):
    if not lst:
        return []
    left_most_pos=0
    for i in range(len(lst)):
        if lst[i]<0:
            lst[i],lst[left_most_pos]=lst[left_most_pos],lst[i]
            left_most_pos+=1
    return lst

lst = [10,-1,20,4,5,-9,-6]
print(rearrange(lst))
