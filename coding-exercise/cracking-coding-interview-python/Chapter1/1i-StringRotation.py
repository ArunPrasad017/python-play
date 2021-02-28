def stringRotate(temp_str, rotate_str):
    if len(temp_str) == len(rotate_str):
        return rotate_str in (temp_str + temp_str)
    return False


str1 = "race"
str2 = "cere"
print(stringRotate(str1, str2))
