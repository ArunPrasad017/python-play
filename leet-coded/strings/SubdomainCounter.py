"""
Input cpdomains is a list
output to be a list of elements with counter adding subdomains and providing output
"""
from nose.tools import assert_equal
import collections


def subdomain_counter(cpdomains):
    counter = collections.Counter()

    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        subdomains = domain.split(".")

        for i in range(0, len(subdomains)):
            counter[".".join(subdomains[i:])] += count
    return ["{} {}".format(k, v) for k, v in counter.items()]


# assert_equal(subdomain_counter(["9001 discuss.leetcode.com"]),["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"])
print(subdomain_counter(["9001 discuss.leetcode.com"]))
