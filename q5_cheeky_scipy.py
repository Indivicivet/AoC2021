from pathlib import Path

import numpy as np
from skimage import draw

lines = Path("input_q5.txt").read_text().splitlines()

vents = np.zeros((1000, 1000))

for line in lines:
    x0, y0, x1, y1 = [int(v) for v in line.replace(" -> ", ",").split(",")]
    if x0 == x1 or y0 == y1:
        vents[draw.line(x0, y0, x1, y1)] += 1

print(np.sum(vents > 1))

vents = np.zeros((1000, 1000))

for line in lines:
    vents[draw.line(*[int(v) for v in line.replace(" -> ", ",").split(",")])] += 1

print(np.sum(vents > 1))
