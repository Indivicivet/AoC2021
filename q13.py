from pathlib import Path

import numpy as np
from PIL import Image

dot_data, instr_data = Path("input_q13.txt").read_text().split("\n\n")

dot_coords = [
    [int(x) for x in line.split(",")]
    for line in dot_data.splitlines()
]

# note to self: axes go x, y!!
dots = np.zeros(np.amax(dot_coords, axis=0) + 1, dtype=int)

for x, y in dot_coords:
    dots[x, y] = 1

pt1 = 0

for line in instr_data.splitlines():
    val = int(line.split("=")[1])
    if "x" in line:
        left = dots[:val, :]
        right = dots[val + 1:, :]
        dots = left + right[::-1, :]
    else:
        top = dots[:, :val]
        bottom = dots[:, val + 1:]
        len_diff = bottom.shape[1] - top.shape[1]
        if len_diff > 0:
            top = np.pad(top, [(0, 0), (len_diff, 0)])
        if len_diff < 0:
            bottom = np.pad(bottom, [(0, 0), (0, -len_diff)])
        dots = top + bottom[:, ::-1]
    if not pt1:
        pt1 = np.sum(dots > 0)


print(pt1)
pt2_data = np.kron(np.pad((dots.T > 0) * 255, 1), np.ones((5, 5)))
Image.fromarray(pt2_data).show()
