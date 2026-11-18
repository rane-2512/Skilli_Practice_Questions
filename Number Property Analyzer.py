def analyzeNumber(n: int) -> dict:
    import math

    is_prime = True

    if n <= 1:
        is_prime = False
    else:
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                is_prime = False
                break

    return {
        "is_even": n % 2 == 0,
        "is_positive": n > 0,
        "is_prime": is_prime,
        "is_perfect_square": n >= 0 and math.isqrt(n) ** 2 == n,
        "digit_count": len(str(abs(n)))
    }
