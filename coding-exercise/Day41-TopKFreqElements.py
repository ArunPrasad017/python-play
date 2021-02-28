def topKFrequent(nums, k):
    """ Pythonic method"""
    # dict1 ={}
    # for num in nums:
    #     if num not in dict1:
    #         dict1[num] = 1
    #     else:
    #         dict1[num]+= 1
    # sorted_list = sorted(dict1.items(), key=lambda x:x[1], reverse=True) # this is a tuple with (k,v)
    # return [sorted_list[i][0] for i in range(k)]

    # heap algorithm? - uses heapq and solves the issue we face of sorting the dictionary
    dict1 ={}
    for num in nums:
        if num not in dict1:
            dict1[num] = 1
        else:
            dict1[num]+= 1
    import heapq
    return heapq.nlargest(k,dict1.keys(), key=dict1.get)



nums = [1,1,2,2,3,3,3,1,1,2,2,2,3,1,1]
k = 2

#nums = [1,2]
#k = 2
print(topKFrequent(nums,k))