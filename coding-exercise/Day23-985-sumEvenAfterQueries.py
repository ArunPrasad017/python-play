"""
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
"""

# def sumEvenAfterQueries(lst,queries):
#     i = 0
#     res = []
#     for val, index in queries:
#         lst[index]+=val
#         sum_val =0
#         for j in range(0,len(lst)):
#             if lst[j]%2==0:
#                 sum_val+=lst[j]
#         res.append(sum_val)
#         i+=1
#     return res


def sumEvenAfterQueries(lst, queries):
    sum_val = sum(x for x in lst if x % 2 == 0)
    ans = []

    for val, index in queries:
        if lst[index] % 2 == 0:
            sum_val -= lst[index]
        lst[index] += val
        if lst[index] % 2 == 0:
            sum_val += lst[index]
        ans.append(sum_val)
    return ans


A = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]

print(sumEvenAfterQueries(A, queries))
