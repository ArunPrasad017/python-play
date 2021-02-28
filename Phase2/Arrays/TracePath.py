def trace_path(my_dict):
    rev_dict = {v: k for k, v in my_dict.items()}
    keys = my_dict.keys()
    res, temp_key = [], 0
    for key in keys:
        if key not in rev_dict:
            res.append([key, my_dict[key]])
            temp_key = my_dict[key]
            break
    to_loc = my_dict[temp_key]
    while to_loc:
        res.append([temp_key, to_loc])
        temp_key = to_loc
        to_loc = my_dict.get(temp_key)
    return res


dict1 = {
    "NewYork": "Chicago",
    "Boston": "Texas",
    "Missouri": "NewYork",
    "Texas": "Missouri",
}

print(trace_path(dict1))
