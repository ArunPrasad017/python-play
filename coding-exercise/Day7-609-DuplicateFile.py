from collections import defaultdict


def findDuplicate(path):
    defaultdict_content = defaultdict(list)
    for c in path:
        s = c.split(" ", 1)
        directory = s[0]
        rest = s[1]
        for f in rest.split(" "):
            name, content = f.split("(")
            content = content.rstrip(")")
            defaultdict_content[content].append(directory + "/" + name)
    res = []
    for key in defaultdict_content.keys():
        res.append(defaultdict_content[key])
    return res


path = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)",
]
print(findDuplicate(path))
