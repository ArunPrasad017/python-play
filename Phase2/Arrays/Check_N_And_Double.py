def check_arr(arr):
    d={i:c for i,c in enumerate(arr)}
    zero_cnt = 0
    for k,v in d.items():
        if v*2 in d.values() and v!=0:
            return True
        if v==0:
            zero_cnt+=1
    if zero_cnt>1:
        return True
    return False

arr = [10,2,5,3]
print(check_arr(arr))

arr = [7,1,20,11]
print(check_arr(arr))