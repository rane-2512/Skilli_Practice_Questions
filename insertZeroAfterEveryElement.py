def insertZeroAfterEveryElement(arr: List[int]) -> List[int]:
    n = len(arr)
    result = []

    for i in range(n):
        result.append(arr[i])
        result.append(0)

    return result[:n]
