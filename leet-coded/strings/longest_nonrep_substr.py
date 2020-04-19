def longest_sub(s):   
    left = 0
    current = 0
    longest = 0
    dict1={}
        
    for right, letter in enumerate(s):
        if letter not in dict1:
            dict1[letter] = right
            current+=1
        else:
            longest = max(current,longest)
            if dict1[letter]>=left:
                left = dict1[letter]+1
            dict1[letter] = right
            current = right - left+1
    longest = max(longest,current)
    return longest

print(longest_sub('aaaaaaa'))