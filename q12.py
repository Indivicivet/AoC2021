from pathlib import Path

pairs = [
    x.split("-")
    for x in Path("input_q12.txt").read_text().splitlines()
]

pairs += [(b, a) for a, b in pairs]


def traverse(route):
    if route[-1] == "end":
        return 1
    return sum(
        traverse(route + [nxt])
        for src, nxt in pairs
        if (
            src == route[-1]
            and (nxt.isupper() or nxt not in route)
        )
    )


def traverse_pt2(route, can_double=True):
    if route[-1] == "end":
        return 1
    if len(route) > 1 and route[-1] == "start":
        return 0
    return sum(
        traverse_pt2(
            route + [nxt],
            can_double and (nxt.isupper() or nxt not in route),
        )
        for src, nxt in pairs
        if (
            src == route[-1]
            and (nxt.isupper() or nxt not in route or can_double)
        )
    )


print(traverse(["start"]))
# print(traverse_pt2(["start"], False))  # check
print(traverse_pt2(["start"]))
