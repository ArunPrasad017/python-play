"""
    implement isunique
    look for ascii or the extended ascii - using ascii here
"""
import unittest
def isunique(string):
    if len(string)>128: return False
    dict_unique = {}
    for c in string:
        if c not in dict_unique:
            dict_unique[c]= True
        else:
            return False
    return True

class myTests(unittest.TestCase):
    def test_assert_equals(self):
        self.assertEquals(isunique("X Æ A-Xii"), False)
        self.assertEquals(isunique("X ÆA-12"), True)
    
if __name__ == "__main__":
    x1 = "X Æ A-Xii"
    x2 = "X ÆA-12"
    print(isunique(x1))
    print(isunique(x2))
    unittest.main()
