"""
Happy Number

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Hint: Use a set and recursion
"""
import pytest

def isHappy(n):
    def get_next(n):
        total_sum = 0 
        while n>0:
            digit = n%10
            n = n//10
            total_sum += digit**2
        return total_sum
    seen = set()
    while n not in seen and n!=1:
        seen.add(n)
        n = get_next(n)
    return n==1

def test_isHappy():
    assert isHappy(19) == True
    assert isHappy(29) == False

n = 19
print(isHappy(n))

test_isHappy()
