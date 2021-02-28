def pair_sum2(arr, k):
    count = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if (arr[i] + arr[j]) == k:
                count += 1
        arr.remove(arr[i])
    print(count)


# Correct solution - using sets


def pair_sum(arr, k):

    if len(arr) < 2:
        return
    # sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))

    return len(output)


# x = pair_sum([1,3,2,2],4)
x = pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)
print(x)
