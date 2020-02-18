# def solution(input):
#     output = []
#     for i in range(0,len(input)):
#         if i%2!=0:
#             output.append(input[i])
#     return output

# assert solution([0,1,2,3,4,5]) == [1,3,5]
# assert solution([1,-1,2,-2]) == [-1,-2]

"""
Write a function that returns the cumulative sum of elements in a list
"""
# def solution(input):
#     output = []
#     for i in range(0,len(input)):
#         if i==0:
#             output.append(input[0])
#         else:
#             output.append(input[i]+output[i-1])
#     return output

# input = [1,1,1]
# print(solution(input))

# assert solution([1,1,1]) == [1,2,3]
# assert solution([1,-1,3]) == [1,0,3]

"""
Write a function that takes a number and returns a list of its digits
"""

# def solution(input):
#     output = []
#     if input < 1:
#         return []
#     while input>=1:
#         output.insert(0, int(input%10))
#         input = input/10
#     return output

# input = 400
# print(solution(input))

# assert solution(123) == [1,2,3]
# assert solution(400) == [4,0,0]
# assert solution(1) == [1]
# assert solution(0.4) == []

"""
Centered Average
"""

# def solution(input):
#     input.sort()
#     sum_val = 0
#     cnt = 0
#     for i in range(1,len(input)-1):
#         cnt+=1
#         sum_val+=input[i]
#     output = int(sum_val/cnt)
#     return output

# assert solution([1, 2, 3, 4, 100]) == 3
# assert solution([1, 1, 5, 5, 10, 8, 7]) == 5
# assert solution([-10, -4, -2, -4, -2, 0]) == -3
