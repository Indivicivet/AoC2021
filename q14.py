from pathlib import Path
from collections import Counter

polymer, _, *replacements = Path("input_q14.txt").read_text().splitlines()

repl_map = dict(x.split(" -> ") for x in replacements)

polymer_pt1 = polymer
for _ in range(10):
    polymer_pt1 = "".join(
        a + repl_map.get(a + b, "")
        for a, b in zip(polymer_pt1, polymer_pt1[1:])
    ) + polymer_pt1[-1]

commons = Counter(polymer_pt1).most_common()
print(commons[0][1] - commons[-1][1])


pairings = Counter()
for a, b in zip(polymer, polymer[1:]):
    pairings[a + b] += 1

elems = Counter(polymer)
for _ in range(40):
    pairings_new = Counter()
    for k, v in pairings.items():
        if k in repl_map:  # "AB": "C"
            to = repl_map[k]
            pairings_new[k[0] + to] += v
            pairings_new[to + k[1]] += v
            elems[to] += v
        else:
            pairings_new[k] += v
    pairings = pairings_new

"""
# alternative method instead of tracking elems as you go:
elems2 = Counter()
for k, v in pairings.items():
    elems2[k[0]] += v
    elems2[k[1]] += v
elems2[polymer[0]] += 1
elems2[polymer[-1]] += 1
# now elems2 contains 2x count of each element
"""

commons_pt2 = elems.most_common()
print(commons_pt2[0][1] - commons_pt2[-1][1])
