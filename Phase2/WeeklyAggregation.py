ts = [
    "2019-01-01",
    "2019-01-02",
    "2019-01-08",
    "2019-02-01",
    "2019-02-02",
    "2019-02-05",
]

output = [
    ["2019-01-01", "2019-01-02"],
    ["2019-01-08"],
    ["2019-02-01", "2019-02-02"],
    ["2019-02-05"],
]

import datetime
from collections import defaultdict


def time_value(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d")


def key_calculator(curr_date, start_date):
    delta = time_value(curr_date) - time_value(start_date)
    return delta.days // 7


def main(ts):
    start_date = ts[0]
    dict_output = defaultdict(list)
    for s in ts:
        key = key_calculator(s, start_date)
        dict_output[key].append(s)
    return dict_output


print(main(ts))
