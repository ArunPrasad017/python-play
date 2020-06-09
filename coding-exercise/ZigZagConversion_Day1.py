"""[summary]
    Input: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this
    P   A   H   N
    A P L S I I G
    Y   I   R

    Output: PAHNAPLSIIGYIR
"""
import unittest
def convert(string,numRows):
    #create a dictionary to help with the traversal and to build string
    dict_string = {}
    pos= 1
    step= 1
    for char in string:
        if pos not in dict_string:
            dict_string[pos] = char
        else:
            dict_string[pos]+=char
        pos+=step
        if pos==numRows or pos==1:
            step*=-1 # reverse the direction whenever you're at the extreme ends 
    # create the modified string from dict
    string_final = ""
    for i in range(1,len(dict_string)+1):
        string_final+=dict_string[i]
    return string_final

# class for unit tests
class mytests(unittest.TestCase):
    def test_assertequals(self):
        self.assertEqual(convert(string, numRows),"PINALSIGYAHRPI")

if __name__ == "__main__":
    string = "PAYPALISHIRING"
    numRows = 4
    # self test 
    print(convert(string,numRows))
    #unit test call
    unittest.main()