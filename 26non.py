
def leftShift(arr: List[int], K: int) -> List[int]:
    result = []

    for i in range(K, len(arr)):
        result.append(arr[i])

    while len(result) < len(arr):
        result.append(0)

    return result
