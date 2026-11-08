def primesInRange(start: int, end: int) -> list[int]:
    primes = []

    for num in range(start, end + 1):
        if num > 1:
            count = 0

            for i in range(1, num + 1):
                if num % i == 0:
                    count += 1

            if count == 2:
                primes.append(num)

    return primes
