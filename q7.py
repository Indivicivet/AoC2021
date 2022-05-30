from pathlib import Path
import json

crabs = json.loads("[" + Path("input_q7.txt").read_text() + "]")

print(min(
    sum(abs(x - i) for x in crabs)
    for i in range(max(crabs) + 1)
))

print(min(
    sum(abs(x - i) * (abs(x - i) + 1) // 2 for x in crabs)
    for i in range(max(crabs) + 1)
))
