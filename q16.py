from pathlib import Path

data = Path("input_q16.txt").read_text().strip()

b = "".join(
    f"{int(x, base=16):04b}"
    for x in data
)


def recursive_decode(ptr):
    """returns (new ptr, val, total version)"""

    def take(n):
        nonlocal ptr
        ptr += n
        return int(b[ptr - n:ptr], base=2)

    version = take(3)
    type_id = take(3)
    if type_id == 4:  # literal
        val = 0
        while True:
            terminate = take(1) == 0
            val <<= 4
            val += take(4)
            if terminate:
                break
        return ptr, val, version
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
        new_ptr, sub_val, sub_version = recursive_decode(ptr)
        ptr = new_ptr
        subs.append(sub_val)
        version += sub_version
        if ptr - ptr0 >= subs_length:
            break
    return ptr, None, version


_, _, pt1 = recursive_decode(0)
print(pt1)
