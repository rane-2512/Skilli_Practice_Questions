
def deleteAllOccurrences(arr: List[int], X: int) -> List[int]:
    a = 0

    for num in arr:
        if num != X:
            arr[a] = num
            a += 1

    while a < len(arr):
        arr[a] = 0
        a += 1

    return arr
