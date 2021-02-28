def intToRoman(num):
    roman_dict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    res = ""
    for k, v in roman_dict.items():
        while num >= k:
            res += num // k * v
            num %= k
        if num == 0:
            return res


print(intToRoman(58))
