from math import sqrt, ceil
from sys import argv


def rse(array: list[float]) -> float:
    n: int = len(array)
    avg: float = sum(array) / n
    variance: float = sum((avg - value) ** 2 for value in array) / (n - 1)
    std_deviation = sqrt(variance)
    std_err = std_deviation / sqrt(n)
    return std_err / avg * 100


file = argv[1]

with open(file, 'r') as f:
    times: list[float] = []
    for line in f.readlines():
        if len(line.split()) != 2:
            continue

        times.append(float(line.split()[1]))
    rse: float = rse(times)
    print(round(rse, 2))
