from pathlib import Path

import numpy as np
from scipy.ndimage import minimum_filter

data = np.array([
    [int(x) for x in line]
    for line in Path("input_q9.txt").read_text().splitlines()
])

# NOT CORRECT (diagonals) but happens to give the right answer on my input...:
# print(np.sum(1 + data[data == minimum_filter(data, 3)]))

print(np.sum(1 + data[data < minimum_filter(
    data,
    footprint=np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]),
    mode="constant",
    cval=99,
)]))


in_basin = data < 9


def traverse(j0, i0):
    if (
        j0 < 0
        or i0 < 0
        or j0 >= in_basin.shape[0]
        or i0 >= in_basin.shape[1]
        or not in_basin[j0, i0]
    ):
        return 0
    in_basin[j0, i0] = False  # traverse
    return 1 + sum(
        traverse(j0 + dj, i0 + di)
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]
    )


basin_sizes = [
    traverse(j, i)
    for j in range(data.shape[0])
    for i in range(data.shape[1])
]

top = sorted(basin_sizes, reverse=True)
print(top[0] * top[1] * top[2])
