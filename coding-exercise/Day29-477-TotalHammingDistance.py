def totalHammingDistance(nums):
    if len(nums) == 0:
        return 0
    n = len(nums)
    ans = 0
    lst = [0] * 31
    for num in nums:
        i = 0
        while num > 0:
            lst[i] += num & 1
            num >>= 1
            i += 1
    for k in lst:
        ans += k * (n - k)
    return ans


# method2
def totalHammingDistance_leetcode(nums):
    if len(nums) == 0:
        return 0
    n = len(nums)
    ans = 0
    for i in range(32):
        count1 = 0
        count0 = 0
        for j in range(n):
            if (nums[j] >> i) & 1:
                count1 += 1
            else:
                count0 += 1
        ans += count1 * count0
    return ans


nums = [4, 14, 4, 14]
print(totalHammingDistance(nums))
print(totalHammingDistance_leetcode(nums))
