import math
from pathlib import Path


data = Path("input_q16.txt").read_text().strip()

b = "".join(
    f"{int(x, base=16):04b}"
    for x in data
)


OPERATORS = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1],
}


def recursive_decode(ptr):
    """returns (new ptr, val, version numbers)"""

    def take(n):
        nonlocal ptr
        ptr += n
        return int(b[ptr - n:ptr], base=2)

    versions = [take(3)]
    type_id = take(3)
    if type_id == 4:  # literal
        val = 0
        while True:
            terminate = take(1) == 0
            val <<= 4
            val += take(4)
            if terminate:
                break
        return ptr, val, versions
    # operator
    if take(1):  # next11 = num subpackets
        subs_length = 99999
        n_subs = take(11)
    else:  # next 15
        subs_length = take(15)
        n_subs = 99999
    subs = []
    ptr0 = ptr
    for _ in range(n_subs):
        new_ptr, sub_val, sub_versions = recursive_decode(ptr)
        ptr = new_ptr
        subs.append(sub_val)
        versions += sub_versions
        if ptr - ptr0 >= subs_length:
            break
    return ptr, OPERATORS[type_id](subs), versions


_, res, versions = recursive_decode(0)
print(sum(versions))
print(res)
