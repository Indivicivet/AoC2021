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


class PointedStr:
    def __init__(self, s, ptr=0):
        self.s = s
        self.ptr = ptr

    def take(self, n):
        self.ptr += n
        return int(self.s[self.ptr - n:self.ptr], base=2)

    def recursive_decode(self):
        """returns (val, version numbers)"""

        versions = [self.take(3)]
        type_id = self.take(3)
        if type_id == 4:  # literal
            val = 0
            while True:
                terminate = self.take(1) == 0
                val <<= 4
                val += self.take(4)
                if terminate:
                    break
            return val, versions
        # operator
        if self.take(1):  # next11 = num subpackets
            subs_length = 99999
            n_subs = self.take(11)
        else:  # next 15
            subs_length = self.take(15)
            n_subs = 99999
        subs = []
        ptr0 = self.ptr
        for _ in range(n_subs):
            sub_val, sub_versions = self.recursive_decode()
            subs.append(sub_val)
            versions += sub_versions
            if self.ptr - ptr0 >= subs_length:
                break
        return OPERATORS[type_id](subs), versions


res, versions = PointedStr(b).recursive_decode()
print(sum(versions))
print(res)
