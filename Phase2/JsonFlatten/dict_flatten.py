d = {
        'a': 1, 
        'b': 2, 
          'c': {
                'c1': [
                        {'c11': 1, 'c12': 2, 'c13': 3}, {'c21': 1, 'c22': 2, 'c23': 3}
                    ], 
                'd1': [
                    {'d11': 1, 'd12': 2, 'd13': 3}, {'d21': 1, 'd22': 2, 'd23': 3}
                    ]
                }, 
        'x': 1, 
        'y': 2}
def flatten_dict(d):
    res = {}
    for k,v in d.items():
        if type(v) is dict:
            v =[v]
        if type(v) is list:
            for s in v:
                # deeper = 
                res.update({k+'_'+key:val for key,val in flatten_dict(s).items()})
        else:
            res[k] = v
    return res

# print(flatten_dict(d))


# merge two dicts

def mergeDict(d1,d2):
    res = d1.copy()
    res.update(d2)
    return res
d1 ={'a': 1, 'e': 2, 'c': 3, 'd': 4}
d2 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
print(mergeDict(d1,d2))