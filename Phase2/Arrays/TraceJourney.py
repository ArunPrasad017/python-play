def trace_path(dict1):
    res = []
    reverse_dict = {}
    for key in dict1.keys():
        reverse_dict[dict1.get(key)] = key
    from_loc,to_loc = None,None
    keys_rev = reverse_dict.keys()
    for key in dict1.keys():
        if key not in keys_rev:
            from_loc = key
            break
    to_loc = dict1[key]
    while to_loc is not None:
        res.append([from_loc, to_loc])
        from_loc = to_loc
        to_loc = dict1.get(from_loc)
    return res

dict1 = {
  "NewYork": "Chicago",
  "Boston": "Texas",
  "Missouri": "NewYork",
  "Texas": "Missouri"
}

print(trace_path(dict1))