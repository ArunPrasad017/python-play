# def Oneaway(s1,s2):
#     if s1==s2:
#         return True
#     dic1 ={c:1 for c in s1}
#     dic2 ={c:1 for c in s2}
#     count= 0
#     for k,v in dic1.items():
#         if k not in dic2.keys():
#             count+=1
#     return count==1

# s1 = "Hello"
# s2 = "llo"
# print(Oneaway(s1,s2))

"""
Check if a string can converted to another string with a single edit
edit can be insert,delete or edit(when lengths are same).
"""

import pytest

def oneAway(s1,s2):
    if s1==s2:
        return True
    
    if len(s1) == len(s2):
        return oneEditAway(s1,s2)
    if len(s1)+1 == len(s2):
        return oneInsertAway(s1,s2)
    if len(s1)-1 ==len(s2):
        return oneInsertAway(s2,s1)
    
def oneEditAway(s1,s2):
    count = sum(1 for i in range(len(s1)) if s1[i]!=s2[i])
    return count==1

def oneInsertAway(s1,s2):
    index1,index2 = 0,0
    edited = False

    while index1<len(s1) and index2<len(s2):
        if s1[index1] != s2[index2]:
            if edited:
                return False
            edited = True
        else:
            index1+=1
        index2+=1
    return True

def test_oneAway():
    assert oneAway('pale', 'ple') == True
    assert oneAway('pale','bale') == True
    assert oneAway('Ronaldo','Rolando') == False
    assert oneAway('Messi','Dissi') == False
    assert oneAway('don','doni') ==True
