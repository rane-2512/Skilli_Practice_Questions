
def floydsTriangle(n: int) -> list[str]:
    result = []
    num = 1

    for i in range(1, n + 1):
        row = []

        for j in range(i):
            row.append(str(num))
            num += 1

        result.append(" ".join(row))

    return result
