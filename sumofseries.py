def sumOfSeries(n: int, a: int, d: int) -> int:
    total = 0

    for i in range(n):
        total = total + (a + i * d)

    return total
