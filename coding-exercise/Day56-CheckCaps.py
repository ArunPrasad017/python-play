"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)>1:
            is_first_cap = True if ord(word[0]) in range(65,91) else False
            is_second_cap = True if ord(word[1]) in range(65,91) else False
            if is_first_cap and is_second_cap:
                for i in range(2,len(word)):
                    if ord(word[i]) not in range(65,91):
                        return False
            elif is_first_cap and not is_second_cap:
                for i in range(2,len(word)):
                    if ord(word[i]) not in range(97,123):
                        return False
            else:
                for i in range(1, len(word)):
                    if ord(word[i]) not in range(97,123):
                        return False
            return True
        else:
            return True