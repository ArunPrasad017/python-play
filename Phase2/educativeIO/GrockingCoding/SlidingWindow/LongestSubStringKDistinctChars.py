def longest_substring_with_k_distinct(str1, k):
    map = {}
    start,max_len = 0,0
    for end in range(len(str1)):
        end_char = str1[end]
        if end_char not in map:
            map[end_char]=0
        map[end_char]+=1
        while len(map)>k:
            start_char = str1[start]
            map[start_char]-=1
            if map[start_char]==0:
                del map[start_char]
            start+=1
        max_len = max(max_len, end-start+1)
    return max_len

print(longest_substring_with_k_distinct("araaci", 2))