from pathlib import Path
from itertools import permutations

from tqdm import tqdm

data = Path("input_q8.txt").read_text().splitlines()

pt1 = 0
pt2 = 0

LETTERS = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [0, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6],
]

for d in tqdm(data):
    clues_raw, signal_raw = d.split(" | ")
    clues = clues_raw.split()
    signal = signal_raw.split()
    sorted_clues = [sorted(x) for x in clues]
    sorted_signal = [sorted(x) for x in signal]
    for x in signal:
        if len(x) in [2, 3, 4, 7]:
            pt1 += 1
    for layout in permutations("abcdefg"):
        sorted_strs = [ 
            sorted(layout[val] for val in letter)
            for letter in LETTERS
        ]
        if all(s in sorted_clues for s in sorted_strs):
            pt2 += int("".join(
                str(sorted_strs.index(sig))
                for sig in sorted_signal
            ))
            break
    
print(pt1)
print(pt2)
