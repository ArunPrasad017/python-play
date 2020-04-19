# import collections
# def longestPalindrome(s):
#     ans = 0
#     for v in collections.Counter(s).values():
#         ans+=v//2*2
#         if ans%2==0 and v%2==1:
#             ans+=1
#     return ans
# s = 'abccccdd'
# print(longestPalindrome(s))

# def Palindrome(s,l,r):
#     while l>=0 and r<len(s) and s[l]==s[r]:
#         l-=1
#         r+=1
#     return s[l+1:r]
    
# def longestPalindrome(s):
#     p =''
#     for i in range(len(s)):
#         p1 = Palindrome(s,i,i)
#         p2 = Palindrome(s,i,i+1)
#         p = max([p, p1, p2], key=lambda x: len(x))
#     return p

# s = 'abccccdd'
# print(longestPalindrome(s))

def lengthOfLongestSubstring(s):
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

s = 'abcabcbb'
print(lengthOfLongestSubstring(s))