def fruits_into_baskets(fruits):
      # TODO: Write your code here
    hashmap = {}
    start,max_fruits = 0,0
    for end in range(len(fruits)):
        end_char = fruits[end]
        if end_char not in hashmap:
            hashmap[end_char]=0
        hashmap[end_char]+=1
        while len(hashmap)>2:
            start_char = fruits[start]
            hashmap[start_char]-=1
            if hashmap[start_char]==0:
                del hashmap[start_char]
            start+=1  
        max_fruits=max(max_fruits,end-start+1)
    return max_fruits

print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
