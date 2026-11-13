import math

def digitsInFactorial(n: int) -> int:
    if n <= 1:
        return 1

    total = 0

    for i in range(2, n + 1):
        total += math.log10(i)

    return int(total) + 1
