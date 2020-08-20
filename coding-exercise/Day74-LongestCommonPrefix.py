"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
"""

def longestCommonPrefix(strs):
    if not(strs):
        return ""
    strs = sorted(strs)
    prefix = strs[0]
    for i in range(1,len(strs)):
        temp_str = ""
        for j in range(len(prefix)):
            if prefix[j]==strs[i][j]:
                temp_str+=prefix[j]
            else:
                break
        prefix = temp_str
    return prefix