from pathlib import Path

data = Path("input_q10.txt").read_text().splitlines()

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
scores_pt2 = dict(zip("([{<", range(1, 5)))

openers = dict(zip(")]}>", "([{<"))

pt1 = 0
pt2 = []

for line in data:
    stack = []
    for char in line:
        try:  # close
            opener = openers[char]
            if not stack or stack[-1] != opener:
                pt1 += scores[char]
                break
            stack.pop(-1)
        except KeyError:
            stack.append(char)
    else:  # not corrupted; pt2
        line_total = 0
        while stack:
            line_total *= 5
            line_total += scores_pt2[stack.pop(-1)]
        pt2.append(line_total)

print(pt1)
print(sorted(pt2)[len(pt2) // 2])
