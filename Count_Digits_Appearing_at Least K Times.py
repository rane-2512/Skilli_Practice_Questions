def countFreq(n: int, k: int) -> list[int]:
    freq = [0] * 10

    if n == 0:
        freq[0] = 1

    while n > 0:
        digit = n % 10
        freq[digit] += 1
        n //= 10

    result = []

    for i in range(10):
        if freq[i] >= k:
            result.append(i)

    return result
