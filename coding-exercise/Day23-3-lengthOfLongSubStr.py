"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 


Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def lengthOfLongestSubstring(s):
    if len(s)==1:
        return 1
    left =0
    current =0
    longest =0
    dict1 = {}

    for right,letter in enumerate(s):
        if letter not in dict1.keys():
            dict1[letter] = right
            current+=1
        else:
            longest = max(current,longest)
            if dict1[letter]>=left:
                left = dict1[letter]+1
            dict1[letter] = right
            current =right-left+1
    longest = max(current,longest)
    return longest

string = "ababc"
print(lengthOfLongestSubstring(string))