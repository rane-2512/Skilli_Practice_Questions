
def primesInRange(start: int, end: int) -> list[int]:
    primes = []

    for num in range(start, end + 1):
        if num > 1:
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(num)

    return primes
