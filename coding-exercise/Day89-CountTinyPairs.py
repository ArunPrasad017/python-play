"""
# --------------------From CodeSignal--------------------
You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

Example

For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
countTinyPairs(a, b, k) = 2.

We're considering the following pairs during iteration:

(1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;
(2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;
(3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.
As you can see, there are 2 tiny pairs during the iteration, so the answer is 2.

For a = [16, 1, 4, 2, 14], b = [7, 11, 2, 0, 15], and k = 743, the output should be
countTinyPairs(a, b, k) = 4.

We're considering the following pairs during iteration:

(16, 15). Their concatenation equals 1615, which is greater than 743, so the pair is not tiny;
(1, 0). Their concatenation equals 10, which is less than 743, so the pair is tiny;
(4, 2). Their concatenation equals 42, which is less than 743, so the pair is tiny.
(2, 11). Their concatenation equals 211, which is less than 743, so the pair is tiny;
(14, 7). Their concatenation equals 147, which is less than 743, so the pair is tiny.
There are 4 tiny pairs during the iteration, so the answer is 4.

"""

def countTinyPairs(a, b, k):
    count = 0
    b[:]=b[::-1]
    for i,j in zip(a,b):
        if int(str(i)+str(j)) <k:
            count+=1
    return count

# 2 lines
def countTinyPairs2(a, b, k):
    b[:]=b[::-1]
    return sum(1 for i,j in zip(a,b) if int(str(i)+str(j)) <k)

