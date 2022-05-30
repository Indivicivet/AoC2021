from pathlib import Path
import numpy as np

raw_numbers, *raw_boards = Path("input_q4.txt").read_text().split("\n\n")

numbers = [int(x) for x in raw_numbers.split(",")]
boards = [
    np.array([
        [int(x) for x in line.split()]
        for line in board.splitlines()
    ])
    for board in raw_boards
]

for i in range(len(numbers)):
    for board in boards:
        scored = np.isin(board, numbers[:i + 1])
        if any(
            all(line)
            for arr in [scored, scored.T]
            for line in arr
        ):
            print(np.sum(board * (1 - scored)) * numbers[i])
            exit()
