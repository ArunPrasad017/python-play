# 
SOME_DATA = [
    {'model': u'Yaris', 'some_value': 11202, 'trim_name': u'3-Door L Manual'},
    {'model': u'Yaris', 'some_value': 19269, 'trim_name': u'3-Door LE Automatic'},
    {'model': u'Corolla', 'some_value': 27119, 'trim_name': u'L Automatic'},
    {'model': u'Corolla', 'some_value': 32262, 'trim_name': u'LE'},
    {'model': u'Corolla', 'some_value': 37976, 'trim_name': u'S Premium'},
    {'model': u'Camry', 'some_value': 39730, 'trim_name': u'LE 4-Cyl'},
    {'model': u'Camry', 'some_value': 45761, 'trim_name': u'XSE 4-Cyl'},
    {'model': u'Yaris', 'some_value': 48412, 'trim_name': u'3-Door L Automatic'},
    {'model': u'Camry', 'some_value': 55423, 'trim_name': u'XLE 4-Cyl'},
    {'model': u'Corolla', 'some_value': 57055, 'trim_name': u'ECO Premium'},
    {'model': u'Corolla', 'some_value': 61296, 'trim_name': u'ECO Plus'},
    {'model': u'Camry', 'some_value': 63660, 'trim_name': u'XSE V6'},
    {'model': u'Yaris', 'some_value': 65570, 'trim_name': u'5-Door LE Automatic'},
    {'model': u'Camry', 'some_value': 67461, 'trim_name': u'XLE V6'},
    {'model': u'Corolla', 'some_value': 73602, 'trim_name': u'S'},
    {'model': u'Yaris', 'some_value': 74158, 'trim_name': u'5-Door SE Manual'},
    {'model': u'Corolla', 'some_value': 74249, 'trim_name': u'LE Plus'},
    {'model': u'Corolla', 'some_value': 78386, 'trim_name': u'ECO'},
    {'model': u'Camry', 'some_value': 82747, 'trim_name': u'SE 4-Cyl'},
    {'model': u'Corolla', 'some_value': 83162, 'trim_name': u'LE Premium'},
    {'model': u'Corolla', 'some_value': 84863, 'trim_name': u'S Plus Manual'},
    {'model': u'Yaris', 'some_value': 90313, 'trim_name': u'5-Door L Automatic'},
    {'model': u'Corolla', 'some_value': 90452, 'trim_name': u'L Manual'},
    {'model': u'Yaris', 'some_value': 93152, 'trim_name': u'5-Door SE Automatic'},
    {'model': u'Corolla', 'some_value': 94973, 'trim_name': u'S Plus CVT'},
]
from collections import defaultdict
# group by of a dictionary
grouped = defaultdict(list)
for item in SOME_DATA:
    grouped[item['model']].append(item)
# print(grouped)
# for k,v in grouped.items():
    # print(v)

lst = [('Rain',1,101,200.0,'2020-01-01'), 
        ('Train',2,102,300.0,'2020-10-10'),
        ('Brain',3,103,400.0,'2020-01-02'),
        ('Brain',3,103,400.0,'2020-01-01')]
        
tuple_grouped = defaultdict(int)
for item in lst:
    tuple_grouped[item[0],item[4]]+=item[3]
# print(tuple_grouped)
# from collections import OrderedDict
# # inventory flow
# lst = [(1,1,'I',10), 
#         (1,2,'I',1),
#         (1,3,'O',2),
#         (1,4,'O',7),
#         (1,5,'O',2)]
# fifo_in,fifo_out = OrderedDict(),OrderedDict()
# res = {}

# for i,item in enumerate(lst):
#     if item[2]=='I':
#         fifo_in[i]=tuple(item)

# for i,item in enumerate(lst):
#     if item[2]=='O':
#         fifo_out[i]=tuple(item)
# i,sum_val=0,0
# print(fifo_out)
# for k,v in fifo_out.items():
#     if (fifo_in[i][3] - (v[3]+sum_val))>0:
#         res[j] = (v[0],fifo_in[i][1],v[1],v[3])
#         sum_val+=v[3]


#### recursive function
import json
# from collections import OrderedDict
# def flatten(d):
#     out = {}
#     def flatten_json(d,name=''):
#         if type(d) is dict:
#             for i in d:
#                 flatten_json(d[i], name+i+'_')
#         elif type(d) is list:
#             i=0
#             for j in d:
#                 flatten_json(d[i], name+str(i)+'_')
#                 i+=1
#         else:
#             out[name[:-1]]=d
#     flatten_json(d)
#     return out

def flatten_json(d):
    res = {}
    if not d:
        return res
    def recurse(d,name=''):
        if type(d) is list:
            i=0
            for j in d:
                recurse(d[i],name+str(i)+'_')
                i+=1
        elif type(d) is dict:
            for it in d:
                recurse(d[it],name+it+'_')
        else:
            res[name[:-1]]=d
    recurse(d)
    return res

test = {
    "employment_history": [
        {
            "company": "Black Belt Academy"
        },
        {
            "company": "Zerion Software",
            "title": "Solutions Engineer"
        }
    ],
    "education": {
        "bachelors": "Information Technology",
        "masters": "Applied Information Technology",
        "phd": "Higher Education"
    }
}
# print(flatten_json(test))

def flatten_list(lst):
    res = []
    def recurse(lst):
        for d in lst:
            if type(d) is list:
                res.extend(recurse(d))
            else:
                res.append(d)
    recurse(lst)
    return res

lst = [1,[1]]
# res = [1,2,3,1,2,3]
print(flatten_list(lst))