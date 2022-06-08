from pathlib import Path

from tqdm import tqdm
import numpy as np

data = np.array([
    [int(x) for x in line]
    for line in Path("input_q15.txt").read_text().splitlines()
])

best = np.full_like(data, 9999)
best[0, 0] = 0

for _ in tqdm(range(999)):
    for y in range(best.shape[0]):
        for x in range(best.shape[1]):
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                try:
                    could_be = best[y + dy, x + dx] + data[y, x]
                    if could_be < best[y, x]:
                        best[y, x] = could_be
                except IndexError:
                    continue

print(best[-1, -1])

h, w = data.shape
data2 = np.zeros((h * 5, w * 5), dtype=int)
for j in range(5):
    for i in range(5):
        region = np.s_[j * h:(j + 1) * h, i * w:(i + 1) * w]
        data2[region] = data
        for _ in range(i + j):
            data2[region] %= 9
            data2[region] += 1

best2 = np.full_like(data2, 9999)
best2[0, 0] = 0

# VERY BAD (SLOW) WAY TO DO THE SECOND PART
for _ in tqdm(range(2500)):
    for y in range(best2.shape[0]):
        for x in range(best2.shape[1]):
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                try:
                    could_be = best2[y + dy, x + dx] + data2[y, x]
                    if could_be < best2[y, x]:
                        best2[y, x] = could_be
                except IndexError:
                    continue

print(best2[-1, -1])
