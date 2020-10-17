"""
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
"""

from collections import defaultdict
def mostCommonWord(paragraph, banned):
    dict1=defaultdict(int)
    banned_set = set(banned)
    s = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
    words= s.split()
    for word in words:
        if word.lower() not in banned_set:
            dict1[word]+=1
    return max(sorted(dict1.keys()),key=dict1.get)

paragraph =  "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(mostCommonWord(paragraph,banned))