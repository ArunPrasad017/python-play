ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
]

output = [
    ['2019-01-01', '2019-01-02'], 
    ['2019-01-08'], 
    ['2019-02-01', '2019-02-02'],
    ['2019-02-05'],
]
from datetime import datetime
from collections import defaultdict
def read_date(date):
    return datetime.strptime(date, '%Y-%m-%d')
def key_weeks(start_date, curr_date):
    return (read_date(curr_date) - read_date(start_date)).days//7
def group_week(ts):
    dict1 = defaultdict(list)
    first_date = ts[0]
    for curr_date in ts:
        dict1[key_weeks(first_date,curr_date)].append(curr_date)
    return dict1.values()

print(group_week(ts))