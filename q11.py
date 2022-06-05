from pathlib import Path

import numpy as np
from scipy import signal


data = np.array([
    [int(c) for c in line]
    for line in Path("input_q11.txt").read_text().splitlines()
])

pt1 = 0
pt2 = 0

for i in range(99999):
    data += 1
    while (flashes := data > 9).any():
        data += signal.convolve(
            flashes,
            np.ones((3, 3)),
            mode="same"
        ).astype("uint8")
        data[flashes] = -9999
        if i < 100:
            pt1 += np.sum(flashes)
    data[data < 0] = 0
    if not data.any():
        pt2 = i + 1
        break

print(pt1)
print(pt2)
