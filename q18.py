from pathlib import Path


def str_to_tree_coordinates(s):
    """represent a tree as a map from binary left/right sequence to a value"""
    tree = {}
    pos = []
    for c in s:
        if c == "[":
            pos.append(0)
        elif c == "]":
            pos.pop()
        elif c == ",":
            pos[-1] = 1
        else:
            tree[tuple(pos)] = int(c)
    return tree


def explode_in_place(num):
    """returns whether exploded"""
    try:
        k0 = min(k for k in num if len(k) > 4)
    except ValueError:  # min throws ValueError
        return False
    stem = k0[:-1]
    v0 = num.pop(k0)
    v1 = num.pop(stem + (1,))
    num[stem] = 0
    try:
        num[max(k for k in num if k < stem)] += v0
    except ValueError:
        pass
    try:
        num[min(k for k in num if k > stem)] += v1
    except ValueError:
        pass
    return True


def split_in_place(num):
    """returns whether split"""
    try:
        k0 = min(k for k, v in num.items() if v > 9)
    except ValueError:
        return False
    v = num.pop(k0)
    num[k0 + (0,)] = v // 2
    num[k0 + (1,)] = v - v // 2
    return True


def add(*nums):
    # generates non-binary tree if more than 2 nums :)
    res = {
        (i,) + k: v
        for i, num in enumerate(nums)
        for k, v in num.items()
    }
    while explode_in_place(res) or split_in_place(res):
        pass  # !!!!
    return res


def magnitude(num):
    # 0s (left) * by 3, 1s (right) * by 2
    return sum(
        v * 2 ** sum(k) * 3 ** (len(k) - sum(k))
        for k, v in num.items()
    )


snailfishes = [
    str_to_tree_coordinates(x)
    for x in Path("input_q18.txt").read_text().splitlines()
]

current = snailfishes[0]
for nxt in snailfishes[1:]:
    current = add(current, nxt)

print(magnitude(current))
