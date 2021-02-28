from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph, banned):
        # two methods
        dic1 = defaultdict(int)
        banned_set = set(banned)
        para_list = [
            ("".join(e for e in word if e.isalnum())).lower()
            for word in paragraph.split()
        ]

        print(para_list)
        for e in para_list:
            if e not in banned_set:
                dic1[e] += 1
        # return max(dic1,key=dic1.get)
        return max(dic1.items(), key=operator.itemgetter(1))[0]
