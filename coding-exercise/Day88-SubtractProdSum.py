def subtractProductAndSum(n):
    prod, sumVal = 1, 0
    while n > 0:
        rem = n % 10
        sumVal += rem
        prod *= rem
        n //= 10
    return prod - sumVal


# n = 234
# print(subtractProductAndSum(n))


from collections import defaultdict


def groupingDishes(dishes):
    ingredient_dict = defaultdict(list)
    for dish in dishes:
        dishName = dish[0]
        for ing in dish[1:]:
            ingredient_dict[ing].append(dishName)
    res_dishes = []
    for key, value in ingredient_dict.items():
        if len(ingredient_dict[key]) < 2:
            continue
        res_dishes.append([key] + value)
    return res_dishes


dishes = [
    ["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
    ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
    ["Quesadilla", "Chicken", "Cheese", "Sauce"],
    ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"],
]
# print(groupingDishes(dishes))


from collections import defaultdict


def areFollowingPatterns(strings, patterns):
    keyList = []
    dict1 = defaultdict(list)
    for i, c in enumerate(strings):
        dict1[i].append(c)
        keyList.append(i)
    for i, c in enumerate(patterns):
        dict1[i].append(c)
        if i not in keyList:
            keyList.append(i)
    keyList.sort()
    cnt = 0
    if len(keyList) > 1:
        for i in range(1, len(keyList)):
            if dict1[i - 1][0] != dict1[i][0] or dict1[i - 1][1] != dict1[i][1]:
                continue
            else:
                return False
    return False


strings = ["cat", "dog", "doggy"]
patterns = ["a", "b", "b"]
print(areFollowingPatterns(strings, patterns))
