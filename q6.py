from collections import Counter
from pathlib import Path
import json

from tqdm import tqdm

fishes = json.loads("[" + Path("input_q6.txt").read_text() + "]")
fishmap = Counter(fishes)  # for part 2

for _ in tqdm(range(80)):
    for i, fish in enumerate(fishes[:]):
        if fish:
            fishes[i] -= 1
        else:
            fishes[i] = 6
            fishes.append(8)

print(len(fishes))

for _ in tqdm(range(256)):
    spawn = fishmap[0]
    fishmap = Counter({
        i - 1 : n
        for i, n in fishmap.items()
        if i
    })
    fishmap[6] += spawn
    fishmap[8] = spawn

print(sum(fishmap.values()))
