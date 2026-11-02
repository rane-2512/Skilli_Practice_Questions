def countFreq(n: int) -> list[int]:
    freq = [0] * 10

    if n == 0:
        freq[0] = 1
        return freq

    while n > 0:
        digit = n % 10
        freq[digit] += 1
        n //= 10

    return freq
