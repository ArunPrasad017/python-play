"""
"""


def findNumbers(nums):
    even_cnt = 0
    for num in nums:
        cnt = 0
        while num > 0:
            num = num // 10
            cnt += 1
        if cnt > 0 and cnt % 2 == 0:
            even_cnt += 1
    return even_cnt


nums = [12, 345, 2, 6, 7896]
print(findNumbers(nums))
