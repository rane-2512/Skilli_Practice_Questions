def rightShift(arr: List[int], K: int) -> List[int]:
    n = len(arr)

    if K >= n:
        return [0] * n

    return [0] * K + arr[:n-K]
