from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append((timestamp,value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = self.map.get(key,None)
        if res is None:
            return ""
        i = bisect_left(res,(timestamp,chr(127)))
        return res[i-1][1] if i else ""