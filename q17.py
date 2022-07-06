import itertools
from pathlib import Path
import re

x0, x1, y0, y1 = map(int, re.findall(r"-?\d+", Path("input_q17.txt").read_text()))

pt1 = 0
pt2 = 0

# could pick tighter (hence faster+more general bounds) based on x0, x1, y0, y1
for vx, vy in itertools.product(range(1, 1000), range(-1000, 1000)):
    x = 0
    y = 0
    ys = []
    while True:
        x += vx
        y += vy
        ys.append(y)
        if vx > 0:
            vx -= 1
        vy -= 1
        if x > x1 or (y < y0 and vy < 0):
            break
        if x0 <= x <= x1 and y0 <= y <= y1:
            pt1 = max(pt1, *ys)
            pt2 += 1
            break

print(pt1)
print(pt2)
