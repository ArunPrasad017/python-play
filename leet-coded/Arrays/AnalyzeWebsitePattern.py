from collections import defaultdict


def mostVisited(users, times, websites):
    groups: Dict[str, (int, str)] = defaultdict(list)

    for (user, time, website) in zip(users, times, websites):
        groups[user].append([time, website])

    seqs = defaultdict(set)
    for user, timed_website in groups.items():
        timed_website = sorted(timed_website)
        for i in range(1, len(timed_website)):
            for j in range(1, i):
                for k in range(j):
                    seq = (
                        timed_website[k][1],
                        timed_website[j][1],
                        timed_website[i][1],
                    )
                    seqs[seq].add(user)
    max_cnt = max(map(lambda x: len(x), seqs.values()))

    for k, v in seqs.items():
        if len(v) == max_cnt:
            return k


username = [
    "joe",
    "joe",
    "joe",
    "james",
    "james",
    "james",
    "james",
    "mary",
    "mary",
    "mary",
]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = [
    "home",
    "about",
    "career",
    "home",
    "cart",
    "maps",
    "home",
    "home",
    "about",
    "career",
]

print(mostVisited(username, timestamp, website))
