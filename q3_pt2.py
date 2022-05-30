from pathlib import Path

data = Path("input_q3.txt").read_text().splitlines()

left_oxy = data.copy()
for i in range(len(data[0])):
    n1 = sum(d[i] == "1" for d in left_oxy)
    n0 = len(left_oxy) - n1
    most_common = "01"[n1 >= n0]  # tie: 1
    left_oxy = [d for d in left_oxy if d[i] == most_common]
    if len(left_oxy) == 1:
        break

left_car = data.copy()
for i in range(len(data[0])):
    n1 = sum(d[i] == "1" for d in left_car)
    n0 = len(left_car) - n1
    least_common = "01"[n1 < n0]  # tie: 0
    left_car = [d for d in left_car if d[i] == least_common]
    if len(left_car) == 1:
        break

print(left_oxy, left_car)
assert len(left_oxy) == 1 and len(left_car) == 1, f"{left_oxy}, {left_car}"
print(int(left_oxy[0], base=2) * int(left_car[0], base=2))

